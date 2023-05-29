from sqlalchemy import desc

from flask_web_poetry import db
from flask_web_poetry.entities.profile_entity import ProfileEntity
from flask_web_poetry.entities.user_entity import UserEntity
from flask_web_poetry.interfaces.user_interface import UserInterface
from flask_web_poetry.models.user_model import UserModel


class UserRepository(UserInterface):
    def create(entity: UserEntity) -> None:
        user_db: UserModel = UserModel(
            name=entity.name, email=entity.email, password_hash=entity.password
        )

        db.session.add(user_db)
        db.session.commit()

    def find_by_email(email: str) -> UserModel:
        user_db: UserModel = UserModel.query.filter_by(email=email).first()
        return user_db

    def update_with_avatar(
        user_db: UserModel, user_entity: ProfileEntity
    ) -> None:
        user_db.name = user_entity.name
        user_db.avatar = user_entity.avatar
        db.session.commit()

    def update(user_db: UserModel, user_entity: ProfileEntity) -> None:
        user_db.name = user_entity.name
        db.session.commit()

    def find_last_register() -> UserModel:
        return UserModel.query.order_by(desc(UserModel.id)).first()
