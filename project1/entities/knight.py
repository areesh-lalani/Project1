

class Knight():
    def __init__(self, knight_id: int, first_name: str, last_name: str, land: str, l_id: int, username: str, password: str):
        self.knight_id = knight_id
        self.first_name = first_name
        self.last_name = last_name
        self.land = land
        self.l_id = l_id
        self.username = username
        self.password = password

    def as_json_dict(self):
        return {
            "knightId": self.knight_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "land": self.land,
            "lId": self.l_id,
            "userName": self.username,
            "passWord": self.password
        }
