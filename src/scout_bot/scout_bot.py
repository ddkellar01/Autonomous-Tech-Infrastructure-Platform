import os
import json
import requests
from datetime import datetime, timedelta

class TechScoutBot:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"token {self.token}"}

    def scout_organization(self, org_name, days_back: int = 7):
        url = f"https://api.github.com/orgs/{org_name}/repos?sort=updated&direction=desc&per_page=10"
        
        # Fixed: Added timeout=10 to comply with zero-trust security and prevent hanging requests (Bandit B113 fix)
        response = requests.get(url, headers=self.headers, timeout=10)
        
        if response.status_code != 200:
            return {'error': f'Failed to fetch {org_name}, status: {response.status_code}'}
        
        repos = response.json()
        summary = []
        cutoff_date = datetime.utcnow() - timedelta(days=days_back)
        
        for repo in repos:
            updated_at = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
            if updated_at >= cutoff_date:
                summary.append({
                    'name': repo['name'],
                    'description': repo['description'],
                    'language': repo['language'],
                    'stars': repo['stargazers_count']
                })
        return summary
