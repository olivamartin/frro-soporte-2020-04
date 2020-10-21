from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from mgclothesstore import db


class Products(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    min_stock = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.id'), nullable=False)
    sex_id = db.Column(db.Integer, db.ForeignKey('sexes.id'), nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('seasons.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.cuit'), nullable=False)
    item_type_id = db.Column(db.Integer, db.ForeignKey('item_types.id'), nullable=False)
    hide = db.Column(db.Integer, nullable=False)

    def __init__(self, code=None, description=None, supplier_id=None, item_type_id=1, sex_id=None, color=None,size_id=None, season_id=None,
                 stock=None, min_stock=None, hide=0):
        self.code = code
        self.description = description
        self.supplier_id = supplier_id
        self.item_type_id = item_type_id
        self.sex_id = sex_id
        self.color = color
        self.size_id = size_id
        self.season_id = season_id
        self.stock = stock
        self.min_stock = min_stock
        self.hide = hide


class Sexes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100))
    addresses = db.relationship('Products', backref='sexes', lazy=True)

    def __init__(self, description=None):
        self.description = description

class Sizes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(5))
    addresses = db.relationship('Products', backref='sizes', lazy=True)

    def __init__(self, description=None):
        self.description = description


class Seasons(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100))
    addresses = db.relationship('Products', backref='seasons', lazy=True)

    def __init__(self, description=None):
        self.description = description


class Suppliers(db.Model):
    cuit = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    addresses = db.relationship('Products', backref='suppliers', lazy=True)
    hide = db.Column(db.Integer, nullable=False)

    def __init__(self, cuit=None, name=None, phone=None, hide=0):
        self.cuit = cuit
        self.name = name
        self.phone = phone
        self.hide = hide


class ItemTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    addresses = db.relationship('Products', backref='item_types', lazy=True)

    def __init__(self, description=None):
        self.description = description


class ProductPrices(db.Model):
    code = db.Column(db.Integer, db.ForeignKey('products.code'), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    cost = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, code=None, date=None, cost=None, price=None):
        self.code = code
        self.date = date
        self.cost = cost
        self.price = price


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.code'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, date=None, product_id=None, amount=None):
        self.date = date
        self.product_id = product_id
        self.amount = amount