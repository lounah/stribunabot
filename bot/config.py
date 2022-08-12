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
    def __init__(self, token: str, port: int, url: str, cert: str, key: str):
        self.port = port
        self.url = url
        self.cert = cert
        self.key = key
        self._token = token

    def token(self) -> str:
        return self._token

    def hook_url(self) -> str:
        return f"{self.url}:{self.port}/{self.token}"
