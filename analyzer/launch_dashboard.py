# analyzer/launch_dashboard.py

import os
import subprocess

def main():
    script_path = os.path.join(os.path.dirname(__file__), "dashboard.py")
    subprocess.run(["streamlit", "run", script_path])
