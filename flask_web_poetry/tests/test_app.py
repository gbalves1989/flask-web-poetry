import json
import os
import unittest
from typing import List

from flask_login import login_user
from werkzeug.datastructures import FileStorage

from flask_web_poetry import app, db
from flask_web_poetry.entities.category_entity import CategoryEntity
from flask_web_poetry.entities.product_entity import ProductEntity
from flask_web_poetry.entities.profile_entity import ProfileEntity
from flask_web_poetry.entities.user_entity import UserEntity
from flask_web_poetry.models.category_model import CategoryModel
from flask_web_poetry.models.product_model import ProductModel
from flask_web_poetry.models.user_model import UserModel
from flask_web_poetry.repositories.category_repository import (
    CategoryRepository,
)
from flask_web_poetry.repositories.product_repository import ProductRepository
from flask_web_poetry.repositories.user_repository import UserRepository
from flask_web_poetry.utils.storage import storage_file


class AppTest(unittest.TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.client = app.test_client()

    def test_1_register_user(self):
        with app.app_context():
            user_entity: UserEntity = UserEntity(
                name='admin',
                email='admin@gmail.com',
                password='administrador2023',
            )

            UserRepository.create(user_entity)
            user_db: UserModel = UserRepository.find_last_register()

            self.assertEqual(user_db.name, 'admin')
            self.assertEqual(user_db.email, 'admin@gmail.com')

    def test_2_login_user(self):
        with app.app_context():
            user_db: UserModel = UserRepository.find_by_email(
                'admin@gmail.com'
            )
            self.assertEqual(user_db.email, 'admin@gmail.com')

            login: bool = user_db.verify_password('administrador2023')
            self.assertEqual(login, True)

    def test_3_update_profile(self):
        with app.app_context():
            user_db: UserModel = UserRepository.find_last_register()

            profile_entity: ProfileEntity = ProfileEntity(
                name='admin test',
            )

            UserRepository.update(user_db, profile_entity)
            user: UserModel = UserRepository.find_last_register()

            self.assertEqual(user.name, 'admin test')

    def test_4_update_avatar_profile(self):
        with app.app_context():
            user_db: UserModel = UserRepository.find_last_register()

            profile_entity: ProfileEntity = ProfileEntity(
                name='admin test',
                avatar='f02eee4f-c738-40d3-a39a-5a7533b15731.jpg',
            )

            UserRepository.update_with_avatar(user_db, profile_entity)
            user: UserModel = UserRepository.find_last_register()

            self.assertEqual(user.name, 'admin test')
            self.assertEqual(
                user.avatar, 'f02eee4f-c738-40d3-a39a-5a7533b15731.jpg'
            )

    def test_5_create_category(self):
        with app.app_context():
            category_entity: CategoryEntity = CategoryEntity(name='bebidas')

            CategoryRepository.create(category_entity)
            category_db: CategoryModel = (
                CategoryRepository.find_last_register()
            )

            self.assertEqual(category_db.name, 'bebidas')

    def test_6_find_category(self):
        with app.app_context():
            category_db: CategoryModel = (
                CategoryRepository.find_last_register()
            )
            category: CategoryModel = CategoryRepository.find_by_id(
                category_db.id
            )

            self.assertEqual(category.id, category_db.id)

    def test_7_find_categories(self):
        with app.app_context():
            categories_db: List[CategoryModel] = CategoryRepository.find_all()
            self.assertNotEqual(categories_db, None)

    def test_8_update_category(self):
        with app.app_context():
            category_db: CategoryModel = (
                CategoryRepository.find_last_register()
            )
            category_entity: CategoryEntity = CategoryEntity(
                name='Energéticos'
            )

            CategoryRepository.update(category_db, category_entity)
            category: CategoryModel = CategoryRepository.find_by_id(
                category_db.id
            )

            self.assertEqual(category.name, 'Energéticos')

    def test_9_delete_category(self):
        with app.app_context():
            category_db: CategoryModel = (
                CategoryRepository.find_last_register()
            )

            category_id: int = category_db.id
            CategoryRepository.delete(category_db)
            category: CategoryModel = CategoryRepository.find_by_id(
                category_id
            )

            self.assertEqual(category, None)

    def test_10_create_product(self):
        with app.app_context():
            category_db: CategoryModel = (
                CategoryRepository.find_last_register()
            )
            product_entity: ProductEntity = ProductEntity(
                name='gatorade', category=category_db
            )

            ProductRepository.create(product_entity)
            product_db: ProductModel = ProductRepository.find_last_register()

            self.assertEqual(product_db.name, 'gatorade')

    def test_11_find_product(self):
        with app.app_context():
            product_db: ProductModel = ProductRepository.find_last_register()
            product: ProductModel = ProductRepository.find_by_id(product_db.id)

            self.assertEqual(product.id, product_db.id)

    def test_12_find_products(self):
        with app.app_context():
            products_db: List[ProductModel] = ProductRepository.find_all()
            self.assertNotEqual(products_db, None)

    def test_13_update_product(self):
        with app.app_context():
            product_db: ProductModel = ProductRepository.find_last_register()
            product_entity: ProductEntity = ProductEntity(
                name='redbull', category=product_db.category
            )

            ProductRepository.update(product_db, product_entity)
            product: ProductModel = ProductRepository.find_by_id(product_db.id)

            self.assertEqual(product.name, 'redbull')

    def test_14_delete_product(self):
        with app.app_context():
            product_db: ProductModel = ProductRepository.find_last_register()

            product_id: int = product_db.id
            ProductRepository.delete(product_db)
            product: ProductModel = ProductRepository.find_by_id(product_id)

            self.assertEqual(product, None)
