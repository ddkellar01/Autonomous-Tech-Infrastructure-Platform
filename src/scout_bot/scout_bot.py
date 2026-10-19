import os
import requests
import json
from datetime import datetime, timedelta

class TechScoutBot:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"token {self.token}"} if self.token else {}

    def scout_organization_repos(self, org_name: str, days_back: int = 7):
        url = f"https://api.github.com/orgs/{org_name}/repos?sort=updated&direction=desc&per_page=10"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code != 200:
            return {"error": f"Failed to fetch {org_name}: {response.status_code}"}

        repos = response.json()
        summary = []
        cutoff_date = datetime.utcnow() - timedelta(days=days_back)

        for repo in repos:
            updated_at = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            if updated_at >= cutoff_date:
                summary.append({
                    "name": repo['name'],
                    "url": repo['html_url'],
                    "description": repo['description'],
                    "language": repo['language'],
                    "stars": repo['stargazers_count']
                })
        return summary
