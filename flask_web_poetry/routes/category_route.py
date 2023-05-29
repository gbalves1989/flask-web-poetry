from flask import Blueprint, render_template
from flask_login import login_required

from flask_web_poetry.forms.category.create_update_form import CreateUpdateForm
from flask_web_poetry.models.category_model import CategoryModel
from flask_web_poetry.services.category_service import CategoryService

category_blueprint = Blueprint(
    'category_routes', __name__, url_prefix='/categories'
)


@category_blueprint.route('/')
@login_required
def page_categories():
    return CategoryService.list_categories()


@category_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def page_create_category():
    form: CreateUpdateForm = CreateUpdateForm()
    return CategoryService.create_category(form)


@category_blueprint.route('/edit/<int:category_id>', methods=['GET', 'POST'])
@login_required
def page_edit_category(category_id: int):
    form: CreateUpdateForm = CreateUpdateForm()
    category_db: CategoryModel = CategoryService.get_category(category_id)
    form.name.data = category_db.name
    return render_template(
        '/category/edit_category.html', category_id=category_id, form=form
    )


@category_blueprint.route('/update/<int:category_id>', methods=['GET', 'POST'])
@login_required
def page_update_category(category_id: int):
    form: CreateUpdateForm = CreateUpdateForm()
    return CategoryService.update_category(category_id, form=form)


@category_blueprint.route('/delete/<int:category_id>', methods=['GET', 'POST'])
@login_required
def page_delete_category(category_id: int):
    return CategoryService.delete_category(category_id)
