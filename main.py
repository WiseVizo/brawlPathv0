from dotenv import load_dotenv
import os
import requests
import json
import urllib.parse
load_dotenv()

api_key = os.getenv("API_KEY3")
print("hm")

tags = ['#9ULYPV8', "#2P89RQGP2"]
tag = urllib.parse.quote(tags[0])
url =  f"https://api.brawlstars.com/v1/players/{tag}"
url2 = "https://api.brawlstars.com/v1/players/#2P89RQGP2"
headers = {
    'Authorization': f'Bearer {api_key}'
}
res = requests.get(url, headers=headers)
print(res.status_code)
if res.status_code == 200:
    res_json = res.json()
    # Save the JSON response to a file
    with open('response.json', 'w') as json_file:
        json.dump(res_json, json_file, indent=4)