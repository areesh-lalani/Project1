from entities.lord import Lord
from daos.lord_dao import LordDao
from daos.lord_dao_postgres import LordDaoPostgres
from abc import ABC, abstractmethod

class LordService(ABC):

    @abstractmethod
    def retrieve_lord_by_user(self, username: str)->Lord:
        pass