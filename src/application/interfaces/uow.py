import typing

from src.application.interfaces.repositories import Repository


class UnitOfWork(typing.Protocol):
    def init(self) -> typing.AsyncContextManager[Repository]: ...
