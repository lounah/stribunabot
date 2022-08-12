from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from bot.consts import LANG_RU, LANG_EN

keyboards = {
    LANG_RU: {
        'start': InlineKeyboardMarkup([
            [InlineKeyboardButton('🗣️ Рассказать о своем проекте', callback_data=str('new_project'))],
            [InlineKeyboardButton('ℹ️ Обо мне', callback_data=str('about'))]
        ]),
        'about': InlineKeyboardMarkup([
            [InlineKeyboardButton('🔙 Назад', callback_data=str('about_back'))],
        ]),
        'publish_project': InlineKeyboardMarkup([
            [InlineKeyboardButton('📨 Отправить на модерацию', callback_data=str('publish_project'))],
        ])
    },
    LANG_EN: {
        'start': InlineKeyboardMarkup([
            [InlineKeyboardButton('🗣️ New idea', callback_data=str('new_project'))],
            [InlineKeyboardButton('ℹ️ About', callback_data=str('about'))]
        ]),
        'about': InlineKeyboardMarkup([
            [InlineKeyboardButton('🔙 Назад', callback_data=str('about_back'))],
        ]),
        'publish_project': InlineKeyboardMarkup([
            [InlineKeyboardButton('Опубликовать', callback_data=str('publish_project'))],
        ])
    }
}
