from services.knight_service import KnightService
from services.knight_service_impl import KnightServiceImpl
from daos.knight_dao import KnightDao
from daos.knight_dao_postgres import KnightDaoPostgres

knight_dao: KnightDao = KnightDaoPostgres()
knight_service: KnightService = KnightServiceImpl(knight_dao)
test_user: str = "uther"

def test_retrieve_knight_by_user():
    result = knight_service.retrieve_knight_by_user(test_user)
    assert result.knight_id == 2