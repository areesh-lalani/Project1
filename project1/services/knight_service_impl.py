from entities.knight import Knight
from daos.knight_dao import KnightDao
from daos.knight_dao_postgres import KnightDaoPostgres
from abc import ABC, abstractmethod
from services.knight_service import KnightService

class KnightServiceImpl(KnightService):

    def __init__(self, knight_dao: KnightDao):
        self.knight_dao = knight_dao

    def retrieve_knight_by_user(self, username: str) -> Knight:
        return self.knight_dao.get_knight(username)

    def retrieve_knights_by_lord(self, l_id):
        return self.knight_dao.get_all_knights_by_lord(l_id)