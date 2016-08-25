import os, time
import re
from slackclient import SlackClient


token = os.environ.get('SLACK_TOKEN')
client = SlackClient(token)

if client.rtm_connect():
    while True:
        last_read = client.rtm_read()
        if last_read:
            try:
                parsed = last_read[0]['text']
                message_channel = last_read[0]['channel']
                if parsed and 'xxx' in parsed:
                    client.rtm_send_message(message_channel, "xxx")
            except:
                pass
        time.sleep(1)
