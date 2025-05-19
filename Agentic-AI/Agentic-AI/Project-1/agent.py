from __future__ import annotations
import json
import re
import os
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
import ollama
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from . import tools

console = Console()

SYSTEM_PROMPT = """
You are an autonomous, tool-using AI agent. Your job is to achieve the user's GOAL by thinking step-by-step
and calling tools when needed. You must ALWAYS respond with a SINGLE-LINE JSON object describing either
a tool call or a final answer. NO natural language outside JSON. NO markdown. NO code fences.

Valid actions and schemas:
1) search:
   {"action":"search","input":"<query string>"}
2) get:
   {"action":"get","input":"<url to fetch>"}
3) write_file:
   {"action":"write_file","path":"<relative_or_absolute_path>","content":"<text to write>"}
4) read_file:
   {"action":"read_file","path":"<relative_or_absolute_path>"}
5) finish:
   {"action":"finish","final_answer":"<your final concise answer (you may include brief bullet points)>"} 

Guidance:
- Prefer search -> get -> summarize to ground your answers with sources.
- When writing files, include the key findings with links (if any).
- Keep going until you can confidently `finish`.
- If earlier steps failed, try alternatives (different search, different URL).
- Be concise and goal-driven.
"""

@dataclass
class AgentConfig:
    model_name: str = os.environ.get("MODEL_NAME", "llama3.1:8b")
    max_steps: int = int(os.environ.get("MAX_STEPS", "8"))

def _extract_first_json(s: str) -> Optional[Dict[str, Any]]:
    # Try a strict parse first
    try:
        return json.loads(s)
    except Exception:
        pass
    # Fallback: find the first {...} blob
    m = re.search(r"\{.*\}", s, flags=re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

class Agent:
    def __init__(self, cfg: Optional[AgentConfig] = None) -> None:
        self.cfg = cfg or AgentConfig()
        self.history: List[Tuple[str, str]] = []  # (action, observation)

    def _chat(self, messages: list) -> str:
        resp = ollama.chat(model=self.cfg.model_name, messages=messages, options={"temperature": 0.2})
        return resp["message"]["content"]

    def _format_scratchpad(self) -> str:
        if not self.history:
            return "Scratchpad:\n"
        lines = ["Scratchpad:"]
        for idx, (action, obs) in enumerate(self.history, start=1):
            obs_short = obs if len(obs) < 1200 else obs[:1200] + "...(truncated)"
            lines.append(f"Step {idx} -> Action: {action}\nObservation: {obs_short}")
        return "\n".join(lines)

    def run(self, goal: str) -> str:
        console.rule(f"[bold blue]Agent starting (max_steps={self.cfg.max_steps})[/]")
        console.print(Panel(f"[bold]GOAL[/]: {goal}"))

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"GOAL: {goal}"},
        ]

        for step in range(1, self.cfg.max_steps + 1):
            scratch = self._format_scratchpad()
            messages_step = messages + [
                {"role": "user", "content": scratch + "\nRespond ONLY with a single-line JSON tool call."}
            ]

            raw = self._chat(messages_step)
            data = _extract_first_json(raw)

            if not data or "action" not in data:
                console.print("[yellow]Model did not return valid JSON. Retrying...[/]")
                messages.append({"role": "user", "content": "Your last output was invalid. Return only a one-line JSON tool call."})
                continue

            action = data.get("action")
            console.print(f"[bold]Step {step}[/]: {action}")

            if action == "search":
                query = data.get("input", "")
                res = tools.search(query, max_results=5)
                formatted = "\n".join(f"- {r['title']} | {r['href']}" for r in res)
                self.history.append((f"search({query})", formatted or "no results"))
            elif action == "get":
                url = data.get("input", "")
                obs = tools.get(url)
                self.history.append((f"get({url})", obs))
            elif action == "read_file":
                path = data.get("path", "")
                obs = tools.read_file(path)
                self.history.append((f"read_file({path})", obs))
            elif action == "write_file":
                path = data.get("path", "")
                content = data.get("content", "")
                obs = tools.write_file(path, content)
                self.history.append((f"write_file({path})", obs))
            elif action == "finish":
                answer = data.get("final_answer", "")
                console.rule("[bold green]FINAL ANSWER[/]")
                console.print(answer)
                return answer
            else:
                self.history.append((f"unknown({action})", "Unsupported action; try again."))

        console.rule("[bold red]GAVE UP[/]")
        console.print("Max steps reached without `finish`. Try increasing MAX_STEPS or refining the goal.")
        return "Max steps reached without finish."
