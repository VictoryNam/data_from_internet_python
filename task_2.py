import requests
import json

token = "02ac83657dccb87789a2ad304fd7396754b1d75a9f6112a496acacaa9a3401c47c2d6d45a346a4bd2916f"
user_id = 18058451
url = f'https://api.vk.com/method/groups.get?user_ids={user_id}&access_token={token}&v=5.131'
params = {"extended": 1,
          "fields": "name" "type"}
responce_vk = requests.get(url, params=params)
vk_json = responce_vk.json()

with open("group_vk", "w") as f:
    json.dump(vk_json, f)
