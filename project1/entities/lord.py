

class Lord:
    def __init__(self, lord_id: int, first_name: str, last_name: str, land: str, username: str, password: str):
        self.lord_id = lord_id
        self.first_name = first_name
        self.last_name = last_name
        self.land = land
        self.username = username
        self.password = password

    def as_json_dict(self):
        return {
            "lordId": self.lord_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "land": self.land,
            "userName": self.username,
            "passWord": self.password
        }
