import os
import requests

# get token and channel_id from environment variables
TOKEN = os.environ('TG_BOT_TOKEN')
CHANNEL_ID = os.environ('CHANNEL_ID')

# target url and data
url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
data = {
    "chat_id": CHANNEL_ID,
    "text": "Hi"
}

# configure request to send a notification
request = requests.post(url, data=data)

if request.status_code != 200:
    raise Exception(f'sending the message failed with an error, { request.content }')
