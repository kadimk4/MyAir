from abc import ABC

from core.interface import BaseInterface


class BaseUser(BaseInterface, ABC):
    pass


class BaseTicket(BaseInterface, ABC):
    pass