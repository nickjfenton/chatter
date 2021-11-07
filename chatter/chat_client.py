from abc import abstractmethod, ABC
from typing import Callable

from chatter.message import Message


class ChatClient(ABC):
    """
    A :class:`ChatClient` handles receiving messages from a chat system,
    (typically through registering some callbacks), transforming these into
    :class:`~chatter.message.Message` format for the chat bot to understand,
    and forwarding these on.

    Any subclass of `ChatClient` must implement two methods:

    * `send_to_client`: allow the bot to send messages to the chat client
    * `start_listening`: allow the bot to begin listening to the chat client
    """

    send_to_bot: Callable[[Message], None]
    """A method bound to the :class:`~chatter.bot.Bot` that handles
    sending messages to it."""

    @abstractmethod
    def send_to_client(self, message: Message):
        """
        Send a message to the chat client.

        Converting the message into a suitable format for the chat
        client is up to the implementing class.
        """

    @abstractmethod
    def start_listening(self) -> None:
        """
        Begin listening to the chat client for messages.

        To forward a message from the chat client to the bot,
        """
