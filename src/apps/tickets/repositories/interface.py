from abc import abstractmethod

from utils.interface import BaseRepository


class BaseTicket(BaseRepository):

    @abstractmethod
    def get_self_tickets(self, *args, **kwargs) -> list:
        raise NotImplementedError
