import sys
from .agent import Agent, AgentConfig
from dotenv import load_dotenv

def main():
    load_dotenv()
    if len(sys.argv) < 2:
        print("Usage: python -m app.main \"<your goal here>\"")
        sys.exit(1)
    goal = sys.argv[1]
    agent = Agent(AgentConfig())
    agent.run(goal)

if __name__ == "__main__":
    main()
