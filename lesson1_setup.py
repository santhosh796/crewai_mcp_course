"""Lesson 1: Setting up CrewAI with MCP Server Access

This lesson shows how to load environment configuration, create a basic CrewAI-style agent,
and execute a simple task in an educational demo mode.
"""

import os
import sys


def load_config():
    fastmcp_url = os.getenv("FASTMCP_URL")
    fastmcp_api_key = os.getenv("FASTMCP_API_KEY")

    if not fastmcp_url or not fastmcp_api_key:
        print("Warning: FASTMCP environment variables are not set. Running in demo fallback mode.")
        return {
            "FASTMCP_URL": "http://demo-fastmcp.local",
            "FASTMCP_API_KEY": "demo-key",
        }

    return {
        "FASTMCP_URL": fastmcp_url,
        "FASTMCP_API_KEY": fastmcp_api_key,
    }


def create_demo_agent():
    try:
        from crewai import Agent
        agent = Agent(name="crewai-basic-agent", description="Beginner CrewAI agent")
        print("Using real CrewAI package.")
        return agent
    except ImportError:
        print("CrewAI package not installed. Running in demo fallback mode.")

        class DemoAgent:
            def __init__(self, name, description):
                self.name = name
                self.description = description

            def run(self, prompt):
                return (
                    "[Demo response] This agent would normally send the prompt to a CrewAI model. "
                    "Prompt: " + prompt
                )

        return DemoAgent("crewai-basic-agent", "Beginner CrewAI agent")


def get_agent_response(agent, prompt):
    if hasattr(agent, "run"):
        return agent.run(prompt)
    if hasattr(agent, "chat"):
        return agent.chat(prompt)
    if hasattr(agent, "prompt"):
        return agent.prompt(prompt)
    raise RuntimeError("Agent object does not support run/chat/prompt methods.")


def main():
    print("Lesson 1: Setup CrewAI with MCP Server Access")
    config = load_config()
    print("Loaded configuration:", {"FASTMCP_URL": config["FASTMCP_URL"]})

    agent = create_demo_agent()
    print("Created agent:", getattr(agent, "name", "<unknown>"))

    prompt = (
        "You are a beginner CrewAI agent. Explain how CrewAI and FastMCP can be used together "
        "to build an intelligent workflow."
    )

    response = get_agent_response(agent, prompt)
    print("\nAgent response:\n")
    print(response)


if __name__ == "__main__":
    main()
