import json
from enum import Enum
from json import JSONEncoder

from telegram import Update

from logger.logger import Logger


class EventType(Enum):
    REPLY = 'REPLY'
    CLICK = 'CLICK'
    COMMAND = 'COMMAND'


class AnalyticsEvent:
    def __init__(self, type: EventType, chat_id: str, desc: str):
        self.type = type
        self.chat_id = chat_id
        self.desc = desc

    @staticmethod
    def from_cmd(update: Update):
        message = update.effective_message
        command = message.text[1: message.entities[0].length]
        return AnalyticsEvent(
            EventType.COMMAND,
            str(update.message.chat_id),
            f'/{command}'
        )

    @staticmethod
    def from_click(update: Update):
        return AnalyticsEvent(
            EventType.CLICK,
            str(update.callback_query.message.chat_id),
            f'{update.callback_query.data}'
        )

    @staticmethod
    def from_reply(update: Update):
        return AnalyticsEvent(
            EventType.REPLY,
            str(update.message.chat_id),
            f'{update.message.text}'
        )


class EventEncoder(JSONEncoder):
    def default(self, event: AnalyticsEvent):
        return {"chat_id": event.chat_id, "type": event.type.value, "desc": event.desc}


class Analytics:
    def __init__(self, logger: Logger):
        self._logger = logger
        self._tag = "Analytics"

    def event(self, event: AnalyticsEvent):
        self._logger.info(self._tag, f'[{event.type.value}] [{event.chat_id}] {event.desc}')
