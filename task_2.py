import requests
import json

token = ""
user_id = ""
url = f'https://api.vk.com/method/groups.get?user_ids={user_id}&access_token={token}&v=5.131'
params = {"extended": 1,
          "fields": "name" "type"}
responce_vk = requests.get(url, params=params)
vk_json = responce_vk.json()

with open("group_vk", "w") as f:
    json.dump(vk_json, f)
