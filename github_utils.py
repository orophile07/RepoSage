import requests
from urllib.parse import urlparse

def extract_github_info(github_url):
    """
    Extracts (owner, repo) from a GitHub URL.
    Example: https://github.com/user/repo → ("user", "repo")
    """
    parts = urlparse(github_url).path.strip("/").split("/")
    if len(parts) >= 2:
        return parts[0], parts[1]
    raise ValueError("Invalid GitHub URL")

def fetch_repo_files(owner, repo):
    """
    Recursively fetches all files in a GitHub repo using GitHub API.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    def get_files(url, collected_files=[]):
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for item in data:
            if item["type"] == "file":
                file_res = requests.get(item["download_url"])
                file_res.raise_for_status()
                collected_files.append({
                    "path": item["path"],
                    "content": file_res.text
                })
            elif item["type"] == "dir":
                get_files(item["url"], collected_files)
        return collected_files

    return get_files(api_url)

def download_file(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.text
