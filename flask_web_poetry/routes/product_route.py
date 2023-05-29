from typing import List

from flask import Blueprint, render_template
from flask_login import login_required

from flask_web_poetry.forms.product.create_form import CreateForm
from flask_web_poetry.forms.product.update_form import UpdateForm
from flask_web_poetry.models.category_model import CategoryModel
from flask_web_poetry.models.product_model import ProductModel
from flask_web_poetry.repositories.category_repository import (
    CategoryRepository,
)
from flask_web_poetry.services.product_service import ProductService

product_blueprint = Blueprint(
    'product_routes', __name__, url_prefix='/products'
)


@product_blueprint.route('/')
@login_required
def page_products():
    return ProductService.list_products()


@product_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def page_create_product():
    form: CreateForm = CreateForm()
    categories_db: List[CategoryModel] = ProductService.list_categories()
    form.category.choices = [
        (category.id, category.name) for category in categories_db
    ]
    return ProductService.create_product(form)


@product_blueprint.route('/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def page_edit_product(product_id: int):
    form: UpdateForm = UpdateForm()
    product_db: ProductModel = ProductService.get_product(product_id)
    category_db: CategoryModel = CategoryRepository.find_by_id(
        product_db.category
    )
    form.name.data = product_db.name

    return render_template(
        '/product/edit_product.html',
        product_id=product_id,
        form=form,
        category_id=category_db.id,
        category_name=category_db.name,
    )


@product_blueprint.route('/update/<int:product_id>', methods=['GET', 'POST'])
@login_required
def page_update_product(product_id: int):
    form: UpdateForm = UpdateForm()
    return ProductService.update_product(product_id, form)


@product_blueprint.route('/delete/<int:product_id>', methods=['GET', 'POST'])
@login_required
def page_delete_product(product_id: int):
    return ProductService.delete_product(product_id)
