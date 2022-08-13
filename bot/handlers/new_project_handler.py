from telegram import ForceReply, ParseMode
from telegram.ext import CallbackQueryHandler, MessageHandler

from analytics.analytics import Analytics, AnalyticsEvent
from bot.consts import PROJECT_REVIEW_CHAT_ID
from bot.repository.products_repository import ProductsRepository
from bot.resources.resources_manager import ResourcesManager
from bot.util.reply_filter import ReplyMessageFilter


class NewProjectHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, analytics: Analytics):
        super().__init__(self._handle, pattern='^new_project$')
        self._resources = resources
        self._analytics = analytics

    def _handle(self, update, ctx):
        self._analytics.event(AnalyticsEvent.from_click(update))
        update.callback_query.message.reply_text(
            self._resources.message('project_description'),
            parse_mode=ParseMode.HTML,
            reply_markup=ForceReply(selective=True)
        )


class ProjectDescriptionHandler(MessageHandler):
    def __init__(self, resources: ResourcesManager, repo: ProductsRepository, analytics: Analytics):
        super().__init__(ReplyMessageFilter(resources.message('project_description')), self._handle)
        self._resources = resources
        self._repo = repo
        self._analytics = analytics

    def _handle(self, update, ctx):
        self._analytics.event(AnalyticsEvent.from_reply(update))
        self._repo.add(update.message.chat_id, update.message.text + ' ' + update.message.from_user.username)
        update.message.reply_text(
            self._resources.message('publish_project'),
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('publish_project')
        )


class PublishProjectHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, repo: ProductsRepository, analytics: Analytics):
        super().__init__(self._handle, pattern='^publish_project$')
        self._resources = resources
        self._repo = repo
        self._analytics = analytics

    def _handle(self, update, ctx):
        ctx.bot.send_message(
            chat_id=PROJECT_REVIEW_CHAT_ID,
            text=self._repo.get(update.callback_query.message.chat_id)
        )
        update.callback_query.edit_message_text(
            self._resources.message('project_published'),
            parse_mode=ParseMode.HTML,
        )
        self._analytics.event(AnalyticsEvent.from_click(update))
