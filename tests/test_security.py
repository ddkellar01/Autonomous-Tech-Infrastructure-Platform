import pytest
from src.security.auditor import SecurityAuditor

def test_security_auditor_init():
    auditor = SecurityAuditor(target_dir="src")
    assert auditor.target_dir == "src"
