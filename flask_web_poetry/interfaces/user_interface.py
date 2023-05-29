from abc import ABC, abstractmethod

from flask_web_poetry.entities.profile_entity import ProfileEntity
from flask_web_poetry.entities.user_entity import UserEntity
from flask_web_poetry.models.user_model import UserModel


class UserInterface(ABC):
    @abstractmethod
    def create(entity: UserEntity) -> None:
        pass

    @abstractmethod
    def find_by_email(email: str) -> UserModel:
        pass

    @abstractmethod
    def update_with_avatar(
        user_db: UserModel, user_entity: ProfileEntity
    ) -> None:
        pass

    @abstractmethod
    def update(user_db: UserModel, user_entity: ProfileEntity) -> None:
        pass
