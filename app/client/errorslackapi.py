import json
import requests

url = "https://hooks.slack.com/services/{{uuid}}"

headers = {
    'Content-Type': "application/json"
    }


def slack(text):
    return requests.request("POST", url, data=json.dumps({"text": ""+text+""}), headers=headers)
