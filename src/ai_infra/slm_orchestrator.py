import json

class SLMAnalyzer:
    def __init__(self, model_path: str = "models/slm-base"):
        self.model_path = model_path

    def summarize_scout_report(self, report_path: str = "scout_report.json") -> str:
        try:
            with open(report_path, "r") as f:
                data = json.load(f)
            
            summary_insights = []
            for org, repos in data.items():
                summary_insights.append(f"Organization {org} has {len(repos)} active updated repositories.")
            
            return " | ".join(summary_insights)
        except FileNotFoundError:
            return "No scout report found to analyze."
