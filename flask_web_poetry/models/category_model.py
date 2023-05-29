from flask_web_poetry import db


class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    products = db.relationship(
        'ProductModel', backref='category_categories', lazy=True
    )
