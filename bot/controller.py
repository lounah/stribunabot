from typing import List

from telegram.ext import Updater, Handler

from bot.config import Config, ReleaseConfig, DebugConfig
from logger.logger import Logger


class BotController:
    def __init__(self, config: Config, handlers: List[Handler]):
        self.updater = Updater(config.token())
        self._handlers = handlers
        self._config = config

    def start(self):
        self._register_handlers()

    def _register_handlers(self):
        for handler in self._handlers:
            self.updater.dispatcher.add_handler(handler)


class DebugBotController(BotController):
    def __init__(self, config: DebugConfig, handlers: List[Handler], logger: Logger):
        super().__init__(config, handlers)
        self._config = config
        self._logger = logger

    def start(self):
        super().start()
        self.updater.start_polling()


class ReleaseBotController(BotController):
    def __init__(self, config: ReleaseConfig, handlers: List[Handler], logger: Logger):
        super().__init__(config, handlers)
        self._config = config
        self._logger = logger

    def start(self):
        super().start()
        self.updater.start_webhook(
            listen="0.0.0.0",
            port=self._config.port,
            url_path=self._config.token(),
            webhook_url=self._config.url + self._config.token()
        )
        self.updater.idle()
