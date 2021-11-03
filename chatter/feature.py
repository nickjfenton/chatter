from typing import Tuple, Callable, Dict

from chatter.queue import Subscriber, Message


class Feature(Subscriber):

    def __init__(self):
        self.subcommands = subcommand.get_subcommand_map(self)

    def receive(self, message: Message):
        if message.text[0] in self.subcommands.keys():
            self.subcommands[message.text[0]](message)


class subcommand:

    TRIGGERS = "subcommand_trigger_words-90aa7c63-a914"
    """This attribute needs to have an underlying random value so that it doesn't
    risk clashing with another attribute that has been set on a fn"""

    def __init__(self, *triggers: str):
        self.triggers: Tuple[str] = triggers

    def __call__(self, func: Callable[[Message], None]):
        setattr(func, subcommand.TRIGGERS, self.triggers)

    @staticmethod
    def _get_all(feature_class: Feature):
        user_commands = []
        for attr_name in dir(feature_class):
            cls_attr = getattr(feature_class, attr_name)
            if callable(cls_attr) and hasattr(cls_attr, subcommand.TRIGGERS):
                user_commands.append(cls_attr)
        return user_commands

    @staticmethod
    def get_subcommand_map(feature_class: Feature) -> Dict[str, Callable[[Message], None]]:
        user_commands = subcommand._get_all(feature_class)
        user_command_mappings = {}
        for cmd in user_commands:
            for command_str in getattr(cmd, subcommand.TRIGGERS):
                user_command_mappings[command_str.lower()] = cmd
        return user_command_mappings
