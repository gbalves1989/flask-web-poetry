from typing import List

from flask import json, render_template

from flask_web_poetry.models.category_model import CategoryModel
from flask_web_poetry.models.product_model import ProductModel
from flask_web_poetry.repositories.category_repository import (
    CategoryRepository,
)
from flask_web_poetry.repositories.product_repository import ProductRepository


class HomeService:
    def list_home() -> str:
        categories_db: List[CategoryModel] = CategoryRepository.find_all()
        products_db: List[ProductModel] = ProductRepository.find_all()

        return render_template(
            'home.html', categories=categories_db, products=products_db
        )
