"""Lesson 3: Advanced CrewAI Patterns with MCP Server

This lesson builds a mini multi-agent workflow using a researcher, writer, and reviewer.
It also shows how agents can share data through the MCP server and validate output.
"""

import os


def load_config():
    fastmcp_url = os.getenv("FASTMCP_URL")
    fastmcp_api_key = os.getenv("FASTMCP_API_KEY")

    if not fastmcp_url or not fastmcp_api_key:
        print("Warning: FASTMCP environment variables are not set. Running this lesson in demo mode.")
        return None, None

    return fastmcp_url, fastmcp_api_key


class DemoAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def respond(self, prompt):
        return f"[{self.role}] Response to prompt: {prompt}"


class DemoMCPStore:
    def __init__(self):
        self.storage = {}

    def save(self, key, data):
        self.storage[key] = data
        return True

    def get(self, key):
        return self.storage.get(key, "<no data>")


def build_agent(role):
    try:
        from crewai import Agent
        return Agent(name=f"crewai-{role}", description=f"{role.capitalize()} agent")
    except ImportError:
        print(f"CrewAI package not installed. Using demo {role} agent.")
        return DemoAgent(name=f"crewai-{role}", role=role)


def run_workflow(researcher, writer, reviewer, mcp_store):
    research_query = "Find the most important CrewAI with FastMCP integration patterns."
    print("Researcher running query:", research_query)
    research_output = researcher.respond(research_query)
    mcp_store.save("research_notes", research_output)

    draft_prompt = (
        "Use the research notes to draft a technical summary.\n"
        f"Research notes: {mcp_store.get('research_notes')}"
    )
    print("\nWriter creating draft...")
    draft_output = writer.respond(draft_prompt)
    mcp_store.save("draft_report", draft_output)

    review_prompt = (
        "Review the draft and suggest improvements.\n"
        f"Draft report: {mcp_store.get('draft_report')}"
    )
    print("\nReviewer checking draft...")
    review_output = reviewer.respond(review_prompt)
    mcp_store.save("review_feedback", review_output)

    final_prompt = (
        "Produce a final report using the draft and reviewer feedback.\n"
        f"Draft report: {mcp_store.get('draft_report')}\n"
        f"Reviewer feedback: {mcp_store.get('review_feedback')}"
    )
    final_report = writer.respond(final_prompt)
    mcp_store.save("final_report", final_report)

    return {
        "research": research_output,
        "draft": draft_output,
        "review": review_output,
        "final": final_report,
    }


def main():
    print("Lesson 3: Advanced CrewAI Patterns with MCP Server")
    load_config()

    researcher = build_agent("researcher")
    writer = build_agent("writer")
    reviewer = build_agent("reviewer")
    mcp_store = DemoMCPStore()

    outputs = run_workflow(researcher, writer, reviewer, mcp_store)

    print("\nWorkflow complete. Final report:\n")
    print(outputs["final"])


if __name__ == "__main__":
    main()
