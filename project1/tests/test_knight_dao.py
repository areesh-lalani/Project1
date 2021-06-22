from daos.knight_dao import KnightDao
from daos.knight_dao_postgres import KnightDaoPostgres
from entities.knight import Knight

knight_dao: KnightDao = KnightDaoPostgres()
test_user: str = "uther"

def test_get_knight():
    result = knight_dao.get_knight(test_user)
    assert result.knight_id == 2
