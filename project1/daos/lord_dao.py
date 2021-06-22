from entities.lord import Lord
from abc import ABC, abstractmethod

class LordDao(ABC):
    @abstractmethod
    def get_lord(self, username: str)-> Lord:
        pass
