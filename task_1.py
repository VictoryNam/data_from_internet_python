import requests
import json

user_name = "VictoryNam"
url = f'https://api.github.com/users/{user_name}/repos'
repos = requests.get(url)
repo_json = repos.json()

for repo in repo_json:
    if repo['private'] == False:
        print(repo['name'])

with open("repo_json", "w") as f:
    json.dump(repo_json, f)



