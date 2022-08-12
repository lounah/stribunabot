from telegram import Message
from telegram.ext import MessageFilter


class ReplyMessageFilter(MessageFilter):
    def __init__(self, msg: str):
        self._msg = msg

    def filter(self, message: Message) -> bool:
        if message.reply_to_message is None:
            return False

        return message.reply_to_message.text == self._msg
