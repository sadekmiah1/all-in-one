import requests

def get_github_repo_contents(owner, repo, path=''):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Example usage
owner = 'sadekmiah1'
repo = 'all-in-one'
contents = get_github_repo_contents(owner, repo)

for item in contents:
    if item['type'] == 'file' and item['name'].endswith('.json'):
        print(f"Found JSON file: {item['name']} - {item['download_url']}")
