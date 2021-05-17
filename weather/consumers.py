import json

from channels.generic.websocket import WebscoketConsumer

class WSConsumer(WebscoketConsumer):
    def connect(self):
        self.accept()