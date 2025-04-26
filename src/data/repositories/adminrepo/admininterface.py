from abc import ABC, abstractmethod


class AdminInterface(ABC):

    @abstractmethod
    def create_default_admin(self):
        pass

    @abstractmethod
    def find_one(self, email):
        pass