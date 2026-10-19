import os
import subprocess

class SecurityAuditor:
    def __init__(self, target_dir="."):
        self.target_dir = target_dir

    def run_bandit_scan(self):
        cmd = ["bandit", "-r", self.target_dir, "-f", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {
            "exit_code": result.returncode,
            "report": result.stdout
        }
