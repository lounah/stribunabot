from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    VERBOSE = 2
    ERROR = 3


class Logger(ABC):

    @abstractmethod
    def debug(self, tag: str, msg: str):
        ...

    @abstractmethod
    def info(self, tag: str, msg: str):
        ...

    @abstractmethod
    def error(self, tag: str, msg: str):
        ...


class LogTarget(ABC):

    @abstractmethod
    def write(self, level: LogLevel, tag: str, msg: str):
        ...


class FileTarget(LogTarget):
    def __init__(self, path: str):
        self._path = path

    def write(self, level: LogLevel, tag: str, msg: str):
        with open(self._path, 'a') as output:
            time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
            output.write(f'{time} [{level.name}] [{tag}] {msg}\n')


class SystemOutTarget(LogTarget):

    def write(self, level: LogLevel, tag: str, msg: str):
        time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        print(f'{time} [{level.name}] [{tag}] {msg}\n')


class LoggerImpl(Logger):
    def __init__(self, targets: [LogTarget]):
        self._targets = targets

    def debug(self, tag: str, msg: str):
        for target in self._targets:
            target.write(LogLevel.DEBUG, tag, msg)

    def info(self, tag: str, msg: str):
        for target in self._targets:
            target.write(LogLevel.INFO, tag, msg)

    def error(self, tag: str, msg: str):
        for target in self._targets:
            target.write(LogLevel.ERROR, tag, msg)
