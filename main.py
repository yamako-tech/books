from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}'


db.create_all()


# CREATE RECORD
new_book = Book(id=3, title='Tokyo Revengers', author="Ken Wakui", rating=10.0)
db.session.add(new_book)
db.session.commit()