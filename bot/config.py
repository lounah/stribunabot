from abc import ABC


class Config(ABC):

    def token(self) -> str:
        pass


class DebugConfig(Config):
    def __init__(self, token: str):
        self._token = token

    def token(self) -> str:
        return self._token


class ReleaseConfig(Config):
    def __init__(self, token: str, port: int, url: str):
        self.port = port
        self.url = url
        self._token = token

    def token(self) -> str:
        return self._token

