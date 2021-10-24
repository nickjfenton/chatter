from abc import abstractmethod, ABC
from typing import List


class Message:
    text: List[str]


class Subscriber(ABC):
    @abstractmethod
    def receive(self, message: Message):
        """Handle a message"""


class MessageQueue:

    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def unsusbcribe(self, subscriber: Subscriber):
        try:
            self._subscribers.remove(subscriber)
        except ValueError:
            pass

    def send(self, message: Message):
        for subscriber in self._subscribers:
            subscriber.receive(message)
