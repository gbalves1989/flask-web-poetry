class ProfileEntity:
    def __init__(self, name: str, avatar: str = ''):
        self.__name = name
        self.__avatar = avatar

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def avatar(self) -> str:
        return self.__avatar

    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar
