from abc import ABC, abstractmethod
from typing import List

from flask_web_poetry.entities.category_entity import CategoryEntity
from flask_web_poetry.models.category_model import CategoryModel


class CategoryInterface(ABC):
    @abstractmethod
    def create(entity: CategoryEntity) -> None:
        pass

    @abstractmethod
    def find_by_id(category_id: int) -> CategoryModel:
        pass

    @abstractmethod
    def find_all() -> List[CategoryModel]:
        pass

    @abstractmethod
    def update(
        category_db: CategoryModel, category_entity: CategoryEntity
    ) -> None:
        pass

    @abstractmethod
    def delete(category_db: CategoryModel) -> None:
        pass
