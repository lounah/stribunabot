from telegram import ParseMode
from telegram.ext import CallbackQueryHandler

from analytics.analytics import Analytics, AnalyticsEvent
from bot.resources.resources_manager import ResourcesManager


class AboutUsHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, analytics: Analytics):
        super().__init__(self._handle, pattern='^about$')
        self._resources = resources
        self._analytics = analytics

    def _handle(self, update, ctx):
        self._analytics.event(AnalyticsEvent.from_click(update))
        update.callback_query.edit_message_text(
            self._resources.message('about'),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=self._resources.keyboard('about')
        )


class AboutUsBackHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, analytics: Analytics):
        super().__init__(self._handle, pattern='^about_back$')
        self._resources = resources
        self._analytics = analytics

    def _handle(self, update, ctx):
        self._analytics.event(AnalyticsEvent.from_click(update))
        update.callback_query.edit_message_text(
            self._resources.message('start'),
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('start')
        )
