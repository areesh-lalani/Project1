from utils.connection_util import connection

def knight_login(username: str, password: str)-> int:
    sql = """ select * from knight where user_name = %s"""
    cursor = connection.cursor()
    cursor.execute(sql, username)
    record = cursor.fetchone()
    if password == record[2]:
        return 1
    return 0

