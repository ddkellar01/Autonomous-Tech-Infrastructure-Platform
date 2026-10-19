import os
import subprocess

class SecurityAuditor:
    def __init__(self, target_dir="."):
        self.target_dir = target_dir

    def run_bandit_scan(self):
        cmd = ["bandit", "-r", self.target_dir, "-f", "json"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            return {
                "exit_code": result.returncode,
                "report": result.stdout
            }
        except FileNotFoundError:
            return {
                "exit_code": 127,
                "report": "Error: bandit tool is not installed or not found in PATH."
            }
