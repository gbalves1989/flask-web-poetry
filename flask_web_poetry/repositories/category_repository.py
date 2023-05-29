from typing import List

from sqlalchemy import desc

from flask_web_poetry import db
from flask_web_poetry.entities.category_entity import CategoryEntity
from flask_web_poetry.interfaces.category_interface import CategoryInterface
from flask_web_poetry.models.category_model import CategoryModel


class CategoryRepository(CategoryInterface):
    def create(entity: CategoryEntity) -> None:
        category_db: CategoryModel = CategoryModel(name=entity.name)

        db.session.add(category_db)
        db.session.commit()

    def find_by_id(category_id: int) -> CategoryModel:
        return CategoryModel.query.filter_by(id=category_id).first()

    def find_all() -> List[CategoryModel]:
        return CategoryModel.query.all()

    def update(
        category_db: CategoryModel, category_entity: CategoryEntity
    ) -> None:
        category_db.name = category_entity.name
        db.session.commit()

    def delete(category_db: CategoryModel) -> None:
        db.session.delete(category_db)
        db.session.commit()

    def find_last_register() -> CategoryModel:
        return CategoryModel.query.order_by(desc(CategoryModel.id)).first()
