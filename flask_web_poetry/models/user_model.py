from flask_login import UserMixin

from flask_web_poetry import bcrypt, db, login_manager


@login_manager.user_loader
def load_user(user_id: int):
    return UserModel.query.get(user_id)


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(180), nullable=True)

    @property
    def password_hash(self) -> str:
        return self.password_hash

    @password_hash.setter
    def password_hash(self, password_text: str) -> None:
        self.password = bcrypt.generate_password_hash(password_text).decode(
            'utf-8'
        )

    def verify_password(self, password_text: str) -> bool:
        return bcrypt.check_password_hash(
            self.password, password_text.encode('utf-8')
        )
