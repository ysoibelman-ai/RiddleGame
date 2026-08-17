
class Player:
    def __init__(self,username:str):
        self.__username = username

    def get_username (self):
        return str(self.__username)

    def rename(self,new_username):
        self.__username = new_username

