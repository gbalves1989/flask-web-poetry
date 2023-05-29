class UserEntity:
    def __init__(self, name: str, email: str, password: str, avatar: str = ''):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__avatar = avatar

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def avatar(self) -> str:
        return self.__avatar

    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar
