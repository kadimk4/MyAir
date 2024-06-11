from abc import ABC, abstractmethod


class BaseInterface(ABC):

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def get_all():
        pass

    @abstractmethod
    def post():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass
