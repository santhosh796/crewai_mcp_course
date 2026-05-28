"""Run all lesson scripts and capture their console output to files in ./outputs/"""
import subprocess
import os

LESSONS = [
    "lesson1_setup.py",
    "lesson2_mcp_integration.py",
    "lesson3_advanced_patterns.py",
]

OUT_DIR = "outputs"

os.makedirs(OUT_DIR, exist_ok=True)

for lesson in LESSONS:
    out_path = os.path.join(OUT_DIR, lesson.replace('.py', '_output.txt'))
    print(f"Running {lesson} -> {out_path}")
    try:
        completed = subprocess.run(["python", lesson], capture_output=True, text=True, timeout=120)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("=== STDOUT ===\n")
            f.write(completed.stdout or "(no stdout)\n")
            f.write("\n=== STDERR ===\n")
            f.write(completed.stderr or "(no stderr)\n")
        print(f"Saved output for {lesson}")
    except Exception as e:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"Error running {lesson}: {e}\n")
        print(f"Error running {lesson}: {e}")

print("All done. See the outputs/ directory.")
