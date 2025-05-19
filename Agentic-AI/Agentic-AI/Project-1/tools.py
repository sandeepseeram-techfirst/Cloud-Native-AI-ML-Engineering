from __future__ import annotations
from typing import List, Dict
from duckduckgo_search import DDGS
import requests
import bs4
import os

def search(query: str, max_results: int = 5) -> List[Dict[str, str]]:
    """Web search via DuckDuckGo. Returns list of dicts with 'title', 'href', 'body'."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "href": r.get("href", ""),
                "body": r.get("body", "")
            })
    return results

def get(url: str, max_chars: int = 2500) -> str:
    """Fetch a URL and extract readable text. Truncates to max_chars."""
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "agentic-ai-demo/1.0"})
        resp.raise_for_status()
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
        pieces = []
        for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
            text = tag.get_text(" ", strip=True)
            if text:
                pieces.append(text)
        text = "\n".join(pieces)
        return text[:max_chars]
    except Exception as e:
        return f"ERROR fetching {url}: {e}"

def read_file(path: str, max_chars: int = 4000) -> str:
    """Read a UTF-8 text file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        return data[:max_chars]
    except Exception as e:
        return f"ERROR reading {path}: {e}"

def write_file(path: str, content: str) -> str:
    """Write a UTF-8 text file, creating parent directories if needed."""
    try:
        parent = os.path.dirname(path)
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"OK: wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"ERROR writing {path}: {e}"
