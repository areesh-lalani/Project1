from entities.knight import Knight
from abc import ABC, abstractmethod

class KnightDao(ABC):
    @abstractmethod
    def get_knight(self, username: str)-> Knight:
        pass

    def get_all_knights_by_lord(self, l_id: int):
        pass