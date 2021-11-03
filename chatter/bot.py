from typing import List

from chatter.chat_client import ChatClient
from chatter.feature import Feature
from chatter.queue import MessageQueue


class Bot:

    def __init__(self, chat_clients: List[ChatClient], features: List[Feature]):
        self.chat_clients = chat_clients

        self.message_queue = MessageQueue()

        for feature in features:
            self.message_queue.subscribe(feature)


