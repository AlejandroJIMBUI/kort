import subprocess
import sys
import os

DIST_DIR = os.path.abspath("dist")
ICON_PATH = os.path.join(DIST_DIR, "favicon.ico")

cmd = [
    sys.executable, "-m", "PyInstaller",
    "main.py",
    "--name", "kort",
    "--windowed",
    "--onefile",
    f"--icon={ICON_PATH}",
    "--add-data", f"{DIST_DIR};dist",
]

subprocess.run(cmd, check=True)