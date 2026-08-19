class Player:
    def __init__(self,username:str):
        self.__username = username

    @property
    def username (self):
        return str(self.__username)

    @username.setter
    def username(self,new_username):
        self.__username = new_username
