from abc import ABC, abstractmethod
from typing import List

from flask_web_poetry.entities.product_entity import ProductEntity
from flask_web_poetry.models.product_model import ProductModel


class ProductInterface(ABC):
    @abstractmethod
    def create(entity: ProductEntity) -> None:
        pass

    @abstractmethod
    def find_all() -> List[ProductModel]:
        pass

    @abstractmethod
    def find_by_id(product_id: int) -> ProductModel:
        pass

    @abstractmethod
    def update(
        product_db: ProductModel, product_entity: ProductEntity
    ) -> None:
        pass

    @abstractmethod
    def delete(product_db: ProductModel) -> None:
        pass
