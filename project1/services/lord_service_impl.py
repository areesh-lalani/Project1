from entities.lord import Lord
from daos.lord_dao import LordDao
from daos.lord_dao_postgres import LordDaoPostgres
from abc import ABC, abstractmethod
from services.lord_service import LordService

class LordServiceImpl(LordService):
    def __init__(self, lord_dao: LordDao):
        self.lord_dao = lord_dao

    def retrieve_lord_by_user(self, username: str) -> Lord:
        return self.lord_dao.get_lord(username)