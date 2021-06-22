from daos.lord_dao import LordDao
from daos.lord_dao_postgres import LordDaoPostgres
from entities.lord import Lord

lord_dao: LordDao = LordDaoPostgres()
test_user: str = "arthur"

def test_get_lord():
    result = lord_dao.get_lord(test_user)
    assert result.lord_id == 2