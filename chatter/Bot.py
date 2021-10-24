from typing import List

from chatter.ChatClient import ChatClient
from chatter.Feature import Feature
from chatter.Queue import MessageQueue


class Bot:

    def __init__(self, chat_clients: List[ChatClient], features: List[Feature]):
        self.chat_clients = chat_clients

        self.message_queue = MessageQueue()

        for feature in features:
            self.message_queue.subscribe(feature)


