from daos.knight_dao import KnightDao
from entities.knight import Knight
from utils.connection_util import connection

class KnightDaoPostgres(KnightDao):
    def get_knight(self, username: str) -> Knight:
        sql = """select * from knight where user_name = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        connection.commit()
        record = cursor.fetchone()
        knight = Knight(int(record[0]), record[1], record[2], record[3], int(record[4]), record[5], record[6])
        #print(str(knight.knight_id) + " " + str(knight.first_name) + " " + str(knight.last_name) + " " +
        #str(knight.land) + " " + str(knight.l_id) + " " + str(knight.username) + " " + str(knight.password))
        return knight

    def get_all_knights_by_lord(self, l_id: int):
        sql = """select * from knight where l_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [l_id])
        connection.commit()
        records = cursor.fetchall()
        knights = []
        for record in records:
            knight = Knight(int(record[0]), record[1], record[2], record[3], int(record[4]), record[5], record[6])
            knights.append(knight.as_json_dict())
        return knights

