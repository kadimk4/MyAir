from apps.tickets.repositories.repository import TicketRepository
from apps.users.repositories.repository import UserRepository
from utils.interface import BaseRepository


class RepositoryFactory:
    repositories: dict[str, type[BaseRepository]] = {'user': UserRepository, 'ticket': TicketRepository, }

    @classmethod
    def create(cls, name: str) -> BaseRepository:
        if name in cls.repositories:
            return cls.repositories[name]()
        raise ValueError('Repository not found: %s' % name)
