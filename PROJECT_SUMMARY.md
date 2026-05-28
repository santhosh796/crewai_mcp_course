# CrewAI MCP Course Project Summary

This repository contains one selected project from the 500 AI Agents collection:

- `lesson1_setup.py` — basic CrewAI setup and demo agent execution
- `lesson2_mcp_integration.py` — FastMCP integration demo workflow
- `lesson3_advanced_patterns.py` — multi-agent researcher/writer/reviewer workflow
- `run_all.py` — runs all lessons and saves outputs locally in `outputs/`

## Demo run details

The lessons are designed to run in demo fallback mode when a real `crewai` or `fastmcp` server is not available.

The output files are generated locally and are not tracked in Git because `outputs/` is in `.gitignore`.

Generated output files:

- `outputs/lesson1_setup_output.txt`
- `outputs/lesson2_mcp_integration_output.txt`
- `outputs/lesson3_advanced_patterns_output.txt`

## How to view the output locally

From the folder `crewai_mcp_course`, run:

```powershell
Get-Content .\outputs\lesson2_mcp_integration_output.txt -Raw
```

## How to add a screenshot for LinkedIn

1. Open `outputs/lesson2_mcp_integration_output.txt` in VS Code or PowerShell.
2. Press `Win + Shift + S` and capture the terminal/output window.
3. Save the screenshot as `outputs/screenshot.png`.
4. Then commit it using:

```powershell
git add outputs/screenshot.png
git commit -m "Add lesson2 output screenshot for LinkedIn"
git push
```

## How to post on LinkedIn

Use this text:

> I published a mini-project demonstrating CrewAI agents integrated with FastMCP. I ran the demos locally (lesson 1–3) in demo fallback mode and captured outputs. Explore the repo: https://github.com/santhosh796/crewai_mcp_course
>
> - Lesson 1: basic agent setup & demo response
> - Lesson 2: FastMCP query integration (demo results)
> - Lesson 3: multi-agent researcher/writer/reviewer workflow
>
> #AI #CrewAI #FastMCP #MachineLearning #LearningJourney
