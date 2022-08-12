from bot.resources.keyboards import keyboards
from bot.resources.messages import messages


class ResourcesManager:
    def __init__(self, lang: str):
        self._locale = lang

    def message(self, key: str) -> str:
        return messages[self._locale][key]

    def keyboard(self, key: str) -> str:
        return keyboards[self._locale][key]
