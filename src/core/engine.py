import json
from src.scout_bot.scout_bot import TechScoutBot
from src.sandbox_runner.sandbox_runner import SandboxRunner

class MasterOrchestrator:
    def __init__(self):
        self.scout = TechScoutBot()
        self.sandbox = SandboxRunner()

    def run_autonomous_cycle(self, orgs):
        master_report = {}
        for org in orgs:
            repos = self.scout.scout_organization_repos(org)
            master_report[org] = repos
        
        with open("scout_report.json", "w") as f:
            json.dump(master_report, f, indent=2)
        return "Autonomous intelligence cycle complete. Report saved."
