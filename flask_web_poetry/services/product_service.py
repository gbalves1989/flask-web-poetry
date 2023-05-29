from typing import List

from flask import Response, flash, json, redirect, render_template, url_for

from flask_web_poetry.entities.product_entity import ProductEntity
from flask_web_poetry.forms.product.create_form import CreateForm
from flask_web_poetry.forms.product.update_form import UpdateForm
from flask_web_poetry.models.category_model import CategoryModel
from flask_web_poetry.models.product_model import ProductModel
from flask_web_poetry.repositories.category_repository import (
    CategoryRepository,
)
from flask_web_poetry.repositories.product_repository import ProductRepository


class ProductService:
    def create_product(form: CreateForm) -> Response | str:
        if form.validate_on_submit():
            product_entity: ProductEntity = ProductEntity(
                name=form.name.data, category=form.category.data
            )
            ProductRepository.create(product_entity)

            flash('Produto cadastrado com sucesso', category='success')
            return redirect(url_for('product_routes.page_create_product'))

        if form.errors != {}:
            for err in form.errors.values():
                flash(f'Erro ao cadastrar o produto {err}', category='error')

        return render_template('/product/create_product.html', form=form)

    def list_products() -> str:
        products_db: List[ProductModel] = ProductRepository.find_all()

        return render_template(
            '/product/list_products.html', products=products_db
        )

    def list_categories() -> List[CategoryModel] | None:
        return CategoryRepository.find_all()

    def get_product(product_id: int) -> ProductModel | None:
        return ProductRepository.find_by_id(product_id)

    def update_product(product_id: int, form: UpdateForm) -> Response | None:
        if form.validate_on_submit():
            product_db: ProductModel = ProductRepository.find_by_id(product_id)
            product_entity: ProductEntity = ProductEntity(
                name=form.name.data, category=product_db.category
            )
            ProductRepository.update(product_db, product_entity)

            flash('Produto atualizado com sucesso', category='success')
            return redirect(url_for('product_routes.page_products'))

        if form.errors != {}:
            for err in form.errors.values():
                flash(f'Erro ao atualizar o produto {err}', category='error')

        return render_template('/product/edit_product.html', form=form)

    def delete_product(product_id: int) -> Response:
        product_db: ProductModel = ProductRepository.find_by_id(product_id)
        ProductRepository.delete(product_db)

        flash('Produto removido com sucesso', category='success')
        return redirect(url_for('product_routes.page_products'))
