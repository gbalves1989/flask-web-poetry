from typing import List

from flask import Response, flash, json, redirect, render_template, url_for

from flask_web_poetry.entities.category_entity import CategoryEntity
from flask_web_poetry.forms.category.create_update_form import CreateUpdateForm
from flask_web_poetry.models.category_model import CategoryModel
from flask_web_poetry.repositories.category_repository import (
    CategoryRepository,
)


class CategoryService:
    def create_category(form: CreateUpdateForm) -> Response | str:
        if form.validate_on_submit():
            category_entity: CategoryEntity = CategoryEntity(
                name=form.name.data
            )
            CategoryRepository.create(category_entity)

            flash('Categoria cadastrada com sucesso', category='success')
            return redirect(url_for('category_routes.page_create_category'))

        if form.errors != {}:
            for err in form.errors.values():
                flash(f'Erro ao cadastrar a categoria {err}', category='error')

        return render_template('/category/create_category.html', form=form)

    def list_categories() -> str:
        categories_db: List[CategoryModel] = CategoryRepository.find_all()

        return render_template(
            '/category/list_categories.html', categories=categories_db
        )

    def get_category(category_id: int) -> CategoryModel | None:
        return CategoryRepository.find_by_id(category_id)

    def update_category(
        category_id: int, form: CreateUpdateForm
    ) -> Response | str:
        if form.validate_on_submit():
            category_db: CategoryModel = CategoryRepository.find_by_id(
                category_id
            )
            category_entity: CategoryEntity = CategoryEntity(
                name=form.name.data
            )
            CategoryRepository.update(category_db, category_entity)

            flash('Categoria atualizada com sucesso', category='success')
            return redirect(url_for('category_routes.page_categories'))

        if form.errors != {}:
            for err in form.errors.values():
                flash(f'Erro ao atualizar a categoria {err}', category='error')

        return render_template('/category/edit_category.html', form=form)

    def delete_category(category_id: int) -> Response:
        category_db: CategoryModel = CategoryRepository.find_by_id(category_id)
        CategoryRepository.delete(category_db)

        flash('Categoria removida com sucesso', category='success')
        return redirect(url_for('category_routes.page_categories'))
