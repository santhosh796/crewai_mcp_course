# CrewAI with FastMCP Server Integration Course

This course teaches beginners how to build CrewAI agents that integrate with data from a FastMCP server.

## What this project includes

- `lesson1_setup.py`: basic CrewAI agent setup and simple prompt execution
- `lesson2_mcp_integration.py`: FastMCP query integration with agent workflows
- `lesson3_advanced_patterns.py`: simple multi-agent workflow with researcher, writer, and reviewer roles
- `run_all.py`: helper script to run every lesson and save outputs in `outputs/`
- `.env.example`: example environment variables file
- `requirements.txt`: dependency list for full package installation

## Recommended Python setup

> Use Python 3.11 or 3.12 on Windows.

Python 3.15 is too new for many prebuilt wheels, so `pip install -r requirements.txt` fails when it tries to build `numpy` from source.

## Quick start (demo mode)

These scripts are written to run in demo fallback mode even if `crewai` and `fastmcp` are not installed.

1. Open PowerShell in the course folder:

```powershell
cd "C:\Users\USER\Downloads\500-AI-Agents-Projects-main\500-AI-Agents-Projects-main\crewai_mcp_course"
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
```

3. Run the lessons in demo mode:

```powershell
python lesson1_setup.py
python lesson2_mcp_integration.py
python lesson3_advanced_patterns.py
```

4. Or run them all and save outputs:

```powershell
python run_all.py
```

## Full install (recommended for real packages)

If you want the real `crewai` and `fastmcp` packages, use Python 3.11 or Conda.

### Option A: Conda (best on Windows)

```powershell
conda create -n crewai python=3.11 -y
conda activate crewai
pip install --upgrade pip setuptools wheel
pip install -r "C:\Users\USER\Downloads\500-AI-Agents-Projects-main\500-AI-Agents-Projects-main\crewai_mcp_course\requirements.txt"
```

### Option B: Python 3.11 venv

1. Install Python 3.11 from python.org.
2. Create a new venv:

```powershell
python3.11 -m venv .venv311
. .\.venv311\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r "C:\Users\USER\Downloads\500-AI-Agents-Projects-main\500-AI-Agents-Projects-main\crewai_mcp_course\requirements.txt"
```

### Option C: Build tools (if you must use Python 3.15)

Install Visual C++ Build Tools, then retry `pip install -r requirements.txt`.

## Environment variables

Create `.env` from `.env.example` or set them in your shell:

```powershell
$env:FASTMCP_URL = "http://your-fastmcp-server-url:port"
$env:FASTMCP_API_KEY = "your-api-key"
```

## Expected output

- `lesson1_setup.py` prints a CrewAI agent startup message and a demo response.
- `lesson2_mcp_integration.py` prints FastMCP query results and an agent response.
- `lesson3_advanced_patterns.py` prints the multi-agent workflow and final report.
- `run_all.py` writes console outputs into `outputs/` for easy review.

## Why this course helps you learn

- Lesson 1 shows basic agent initialization and environment handling.
- Lesson 2 shows how an agent can call an external tool/service and use returned data.
- Lesson 3 shows a simple chain of agent roles and data sharing.
- `run_all.py` shows how to capture outputs for documentation or portfolio work.

## Troubleshooting

- If `pip install -r requirements.txt` fails on `numpy`, you are likely using Python 3.15 on Windows. Use Python 3.11 or Conda instead.
- If `requirements.txt` cannot be found, make sure you are in the course folder.
- If `crewai` or `fastmcp` are not installed, the scripts still run with demo fallback behavior.

## LinkedIn post idea

> I just completed a mini-course project demonstrating CrewAI agent workflows with FastMCP integration. It includes three lessons: setup, MCP integration, and multi-agent collaboration. The repo includes demo fallback mode so the examples can run locally even without cloud access. Feedback welcome!

## Next step

If you want, I can also add:

- `README` screenshots from `outputs/`
- a GitHub Actions workflow to run the lessons automatically
- a real FastMCP example using your server URL and API key

