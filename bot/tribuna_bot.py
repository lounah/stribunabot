import threading

from bot.controller import BotController
from logger.logger import Logger


class TribunaBot:
    def __init__(self, controller: BotController, logger: Logger):
        self._controller = controller
        self._logger = logger
        self._tag = "TribunaBot"

    def start(self):
        self._controller.start()
        # try:
        #     threading.Thread(target=self._controller.start).start()
        # except Exception as e:
        #     self._logger.error(self._tag, f"{str(e)}")
