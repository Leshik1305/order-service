import typing

from .repositories import Repository


class UnitOfWork(typing.Protocol):
    def init(self) -> typing.AsyncContextManager[Repository]: ...
