import requests
import os
from src.Models.ContributorActivity import Repository
from src.Models.GitHubRepository import GitHubRepository
from dotenv import load_dotenv

load_dotenv()


def get_contributors_stats(repo_name: str) -> Repository:
    status_code = 0
    while status_code != 200:
        response = requests.get(
            f"https://api.github.com/repos/THD-C/{repo_name}/stats/contributors",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        status_code = response.status_code
        print(f"{status_code} - {repo_name}")
        
    return Repository(**{"name": repo_name, "activity": response.json()})

def get_repository_list(org_name: str) -> list[GitHubRepository]:
    response = requests.get(
        f"https://api.github.com/orgs/{org_name}/repos",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    return [GitHubRepository(**repo) for repo in response.json()]
