from chatter.queue import Subscriber, Message


class ChatClient(Subscriber):

    def send_to_client(self, message: Message):
        """
        Send messages to a chat client.

        The conversion of the message into a suitable format for the chat
        client is up to the implementing class.
        """

    def send_to_features(self, message: Message):
        pass