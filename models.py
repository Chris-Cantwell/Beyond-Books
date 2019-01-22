import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(64), nullable=False)
    isbn = db.Column(db.String(12), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    year = db.Column(db.String(), nullable=False)

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
