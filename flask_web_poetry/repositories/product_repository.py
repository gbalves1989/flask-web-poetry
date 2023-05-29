from typing import List

from sqlalchemy import desc

from flask_web_poetry import db
from flask_web_poetry.entities.product_entity import ProductEntity
from flask_web_poetry.interfaces.product_interface import ProductInterface
from flask_web_poetry.models.product_model import ProductModel


class ProductRepository(ProductInterface):
    def create(entity: ProductEntity) -> None:
        product_db: ProductModel = ProductModel(
            name=entity.name, category=entity.category
        )

        db.session.add(product_db)
        db.session.commit()

    def find_all() -> List[ProductModel]:
        return ProductModel.query.all()

    def find_by_id(product_id: int) -> ProductModel:
        return ProductModel.query.filter_by(id=product_id).first()

    def update(
        product_db: ProductModel, product_entity: ProductEntity
    ) -> None:
        product_db.name = product_entity.name
        product_db.category = product_entity.category
        db.session.commit()

    def delete(product_db: ProductModel) -> None:
        db.session.delete(product_db)
        db.session.commit()

    def find_last_register() -> ProductModel:
        return ProductModel.query.order_by(desc(ProductModel.id)).first()
