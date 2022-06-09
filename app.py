import requests

TOKEN = 'xoxb-337343413792-3624549796291-C7z6RMc0CCL7IvBpF2EoCwtY'
CHANNEL = 'himitsu_no_hanazono'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
   'channel': CHANNEL,
   'text': 'テストです。'
}
r = requests.post(url, headers=headers, data=data)
print("return ", r.json())