from telegram import ParseMode
from telegram.ext import CommandHandler

from analytics.analytics import Analytics, AnalyticsEvent
from bot.resources.resources_manager import ResourcesManager


class StartHandler(CommandHandler):
    def __init__(self, resources: ResourcesManager, analytics: Analytics):
        super().__init__(['start'], self._handle)
        self._resources = resources
        self._analytics = analytics

    def _handle(self, update, ctx):
        self._analytics.event(AnalyticsEvent.from_cmd(update))
        update.message.reply_text(
            self._resources.message('start'),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('start')
        )
