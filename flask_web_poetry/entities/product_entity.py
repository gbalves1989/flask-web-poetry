class ProductEntity:
    def __init__(self, name: str, category: int):
        self.__name = name
        self.__category = category

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def category(self) -> int:
        return self.__category

    @category.setter
    def category(self, category: int):
        self.__category = category
