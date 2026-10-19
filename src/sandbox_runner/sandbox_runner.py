import subprocess

class SandboxRunner:
    def __init__(self, memory_limit="512m", timeout_sec=120):
        self.memory_limit = memory_limit
        self.timeout_sec = timeout_sec

    def execute_in_sandbox(self, repo_url: str, test_command: str):
        docker_cmd = [
            "docker", "run", "--rm",
            "--network", "none",
            "--memory", self.memory_limit,
            "--cpus", "1.0",
            "python:3.11-slim",
            "bash", "-c",
            f"git clone --depth 1 {repo_url} /app && cd /app && {test_command}"
        ]
        try:
            result = subprocess.run(docker_cmd, capture_output=True, text=True, timeout=self.timeout_sec)
            return {
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except subprocess.TimeoutExpired:
            return {"error": "Execution timed out."}
