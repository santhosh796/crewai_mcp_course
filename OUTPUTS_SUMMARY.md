## Outputs Summary

This repository's lesson runs write human-readable output files into the `outputs/` folder when you run `run_all.py` locally.

- Why this file: The `outputs/` folder is intentionally ignored by Git to avoid committing generated files. This summary provides a visible, shareable overview in the repo root.
- Files generated locally:
  - `outputs/lesson1_setup_output.txt`
  - `outputs/lesson2_mcp_integration_output.txt`
  - `outputs/lesson3_advanced_patterns_output.txt`

How to view the outputs locally (PowerShell):

```powershell
Set-Location "%~dp0"
Get-Content .\outputs\lesson2_mcp_integration_output.txt -Raw
```

If you'd like a screenshot or a single file tracked in the repo (for LinkedIn), save the image as `outputs/screenshot.png` and tell me "saved" — I will add, commit, and push it for you.

— Maintainer
