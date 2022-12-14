import threading

from bot.controller import BotController
from logger.logger import Logger


class TribunaBot:
    def __init__(self, controller: BotController, logger: Logger):
        self._controller = controller
        self._logger = logger
        self._tag = "TribunaBot"

    def start(self):
        self._logger.debug(self._tag, "Started")
        self._controller.start()
