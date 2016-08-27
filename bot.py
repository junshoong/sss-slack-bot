import time
from config import *
from slackclient import SlackClient
from importlib import import_module

eating = ['밥', '뭐 먹', '뭐먹']
PREFIX = '!'

class Bot(object):

    def __init__(self):
        self.client = SlackClient(SLACK_TOKEN)
        self.apps = self.import_apps()

    def import_apps(self):
        apps = {}
        for app_name in APPS:
            app = import_module('apps.%s' % app_name)
            func = getattr(app, "on_message")
            print("import %s.%s" % (app_name, func))
            apps[app_name] = func

        return apps

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
            if PREFIX != text[0]:
                continue

            command, args = self.extract_text(text)
            app = self.apps.get(command, None)
            if not app:
                continue

            self.client.rtm_send_message(channel, app(args))

    def extract_text(self, text):
        string = text[1:].split(' ', 1)
        command = string[0]
        if len(string) > 1:
            args = string[1]
        else:
            args = None

        return command, args

    def connect(self):
        if not self.client.rtm_connect():
            raise RuntimeError('Connecting Fail.')

        while True:
            commands = self.client.rtm_read()
            if commands:
                messages = self.commands_info(commands)
                self.cognize(messages)

            time.sleep(0.2)

if '__main__' == __name__:
    bot = Bot()
    bot.connect()
