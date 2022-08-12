import os
from typing import List

from telegram.ext import Handler

from analytics.analytics import Analytics
from analytics.analytics_logger import AnalyticsLogger
from bot.handlers.about_us_handler import AboutUsHandler, AboutUsBackHandler
from bot.handlers.new_project_handler import NewProjectHandler, ProjectDescriptionHandler, PublishProjectHandler
from bot.repository.products_repository import ProductsRepository
from bot.tribuna_bot import TribunaBot
from bot.config import DebugConfig, ReleaseConfig
from bot.controller import BotController, DebugBotController, ReleaseBotController
from bot.handlers.start_handler import StartHandler
from bot.resources.resources_manager import ResourcesManager
from logger.logger import LoggerImpl, SystemOutTarget, FileTarget

LOGS_PATH = 'outputs/logs.txt'
ANALYTICS_LOG_PATH = 'outputs/analytics.json'


class Di:
    def __init__(self, token: str, port: str = "", url: str = ""):
        self._token = token
        self._port = port
        self._url = url
        self._logger = LoggerImpl([SystemOutTarget(), FileTarget(LOGS_PATH)])
        self._analytics_logger = AnalyticsLogger(ANALYTICS_LOG_PATH)
        self._analytics = Analytics(self._logger)
        self._resources = ResourcesManager('ru')
        self._products_repo = ProductsRepository()
        self._init_logs()

    def bot(self) -> TribunaBot:
        controller = self._create_controller()
        return TribunaBot(controller, self._logger)

    def _create_controller(self) -> BotController:
        if not self._port and not self._url:
            return DebugBotController(DebugConfig(self._token), self._handlers(), self._logger)
        else:
            config = ReleaseConfig(self._token, int(self._port), self._url)
            return ReleaseBotController(config, self._handlers(), self._logger)

    @staticmethod
    def _init_logs():
        os.makedirs(os.path.dirname(LOGS_PATH), exist_ok=True)

    def _handlers(self) -> List[Handler]:
        return [
            StartHandler(self._resources, self._analytics),
            AboutUsHandler(self._resources, self._analytics),
            AboutUsBackHandler(self._resources, self._analytics),
            NewProjectHandler(self._resources, self._analytics),
            ProjectDescriptionHandler(self._resources, self._products_repo, self._analytics),
            PublishProjectHandler(self._resources, self._products_repo, self._analytics),
        ]
