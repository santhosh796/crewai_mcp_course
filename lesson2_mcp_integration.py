"""Lesson 2: Integrating MCP Server with CrewAI

This lesson demonstrates how a CrewAI agent can use a custom FastMCP tool,
authenticate with the MCP server, and act on retrieved data.
"""

import os
import sys


def load_config():
    fastmcp_url = os.getenv("FASTMCP_URL")
    fastmcp_api_key = os.getenv("FASTMCP_API_KEY")

    if not fastmcp_url or not fastmcp_api_key:
        print("Warning: FASTMCP environment variables are not set. Running in demo fallback mode.")
        return "http://demo-fastmcp.local", "demo-key"

    return fastmcp_url, fastmcp_api_key


class DemoFastMCPClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def query(self, workspace, query_text, top_k=3):
        return [
            {
                "source": "demo-document-1",
                "text": "This is a demo FastMCP result for query: %s" % query_text,
            },
            {
                "source": "demo-document-2",
                "text": "FastMCP can return structured metadata, records, and context for agents.",
            },
        ]


def create_fastmcp_client(base_url, api_key):
    try:
        from fastmcp import MCPClient

        return MCPClient(base_url=base_url, api_key=api_key)
    except ImportError:
        print("FastMCP package not installed. Running in demo fallback mode.")
        return DemoFastMCPClient(base_url, api_key)


def create_agent_with_tool():
    try:
        from crewai import Agent, Tool

        tool = Tool(
            name="fastmcp_query",
            description="Query the FastMCP server for structured data.",
        )

        agent = Agent(
            name="crewai-mcp-agent",
            description="CrewAI agent with FastMCP tool access.",
            tools=[tool],
        )
        print("Created CrewAI agent with real tool support.")
        return agent
    except ImportError:
        print("CrewAI package not installed. Using demo agent with manual FastMCP integration.")

        class DemoAgent:
            def __init__(self, name, description):
                self.name = name
                self.description = description

            def run(self, prompt):
                return (
                    "[Demo Agent] Generated answer from prompt: " + prompt
                )

        return DemoAgent("crewai-mcp-agent", "CrewAI agent with FastMCP tool access.")


def format_fastmcp_results(results):
    lines = ["FastMCP query results:"]
    for item in results:
        lines.append(f"- {item.get('source')}: {item.get('text')}")
    return "\n".join(lines)


def main():
    print("Lesson 2: Integrating MCP Server with CrewAI")
    base_url, api_key = load_config()
    mcp_client = create_fastmcp_client(base_url, api_key)
    agent = create_agent_with_tool()

    query_text = "Retrieve the latest project notes for the CrewAI FastMCP course."
    print("Running FastMCP query...\n")
    fastmcp_results = mcp_client.query("crewai-course", query_text)
    print(format_fastmcp_results(fastmcp_results))

    prompt = (
        "Use the FastMCP results to explain how the CrewAI agent should proceed with the course workflow.\n"
        "Results:\n" + format_fastmcp_results(fastmcp_results)
    )

    if hasattr(agent, "run"):
        response = agent.run(prompt)
    elif hasattr(agent, "chat"):
        response = agent.chat(prompt)
    else:
        response = "[Demo fallback] Agent could not execute the prompt directly."

    print("\nAgent response:\n")
    print(response)


if __name__ == "__main__":
    main()
