import time
from config import *
from slackclient import SlackClient

eating = ['밥', '뭐 먹', '뭐먹']

class Bot(object):

    def __init__(self):
        self.client = SlackClient(SLACK_TOKEN)

    def check_in_read(self, words, parsed):
        if parsed:
            for word in words:
                if word in parsed:
                    return True
        return False

    def commands_info(self, commands):
        messages = []
        for command in commands:
            text = command.get('text', None)
            channel = command.get('channel', None)
            if channel and text:
                messages.append((channel, text))
        return messages

    def cognize(self, messages):
        for channel, text in messages:
            if PREFIX in text:
                continue

            if self.check_in_read(eating, text):
                self.client.rtm_send_message(channel, '학식먹어')

    def connect(self):
        if not self.client.rtm_connect():
            raise RuntimeError('Connecting Fail.')

        while True:
            commands = self.client.rtm_read()
            if commands:
                messages = self.commands_info(commands)
                self.cognize(messages)

            time.sleep(0.01)

if '__main__' == __name__:
    bot = Bot()
    bot.connect()
