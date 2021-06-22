from daos.lord_dao import LordDao
from entities.lord import Lord
from utils.connection_util import connection

class LordDaoPostgres(LordDao):
    def get_lord(self, username: str) -> Lord:
        sql = """select * from lord where user_name = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        connection.commit()
        record = cursor.fetchone()
        knight = Lord(int(record[0]), record[1], record[2], record[3], (record[4]), record[5])
        return knight
