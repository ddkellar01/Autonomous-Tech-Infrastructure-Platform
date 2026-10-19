import pytest
from src.sandbox_runner.sandbox_runner import SandboxRunner

def test_sandbox_defaults():
    runner = SandboxRunner(memory_limit="256m", timeout_sec=60)
    assert runner.memory_limit == "256m"
    assert runner.timeout_sec == 60
