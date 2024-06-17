from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get(self, *args, **kwargs) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, *args, **kwargs) -> list:
        raise NotImplementedError

    @abstractmethod
    def post(self, *args, **kwargs) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, *args, **kwargs) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs) -> dict | None:
        raise NotImplementedError
