import json
from datetime import datetime

from logger.logger import Logger, LogTarget, LogLevel


class AnalyticsLoggerTarget(LogTarget):
    def __init__(self, path: str):
        self._path = path

    def write(self, level: LogLevel, tag: str, msg: str):
        with open(self._path, 'a') as output:
            time = str(datetime.now())
            output.write(str(json.loads(msg) | {"time": time}) + ', \n')


class AnalyticsLogger(Logger):
    def __init__(self, path: str):
        self._target = AnalyticsLoggerTarget(path)

    def info(self, tag: str, msg: str):
        self._target.write(LogLevel.INFO, tag, msg)

    def debug(self, tag: str, msg: str):
        pass

    def error(self, tag: str, msg: str):
        pass
