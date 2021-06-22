from entities.knight import Knight
from daos.knight_dao import KnightDao
from daos.knight_dao_postgres import KnightDaoPostgres
from abc import ABC, abstractmethod

class KnightService(ABC):

    @abstractmethod
    def retrieve_knight_by_user(self, username: str)->Knight:
        pass

    @abstractmethod
    def retrieve_knights_by_lord(self, l_id):
        pass