from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Optional, Email, NumberRange, Length, ValidationError, LessThanMinStock, LessThanCost, EqualTo,MoreThanMaxDate,LessThanMinDate
from mgclothesstore.models import db, Suppliers, Seasons, ItemTypes, Sexes, ProductPrices, Products, Sales
import re


# Custom validations
def validate_product_exists(form, field):
    new_product = Products.query.filter_by(code=field.data).first()
    if new_product:
        raise ValidationError("El producto ya existe")


def validate_product_not_exists(form, field):
    new_product = Products.query.filter_by(code=field.data).first()
    if not new_product:
        raise ValidationError("El producto no existe")


def check_supplier(form, field):
    new_supplier = Suppliers.query.filter_by(name=re.sub(":|=|¿|¡|}|_|´| |-|!|'|·|#|%|&|/|¨", "", field.data)).first()
    if not new_supplier:
        raise ValidationError('El proveedor no existe')


def check_item_type(form, field):
    new_item_type = ItemTypes.query.filter_by(description=field.data).first()
    if not new_item_type:
        raise ValidationError('El tipo de prenda no existe')


def validate_supplier_cuit_exists(form, field):
    new_supplier = Suppliers.query.filter_by(cuit=field.data).first()
    if new_supplier:
        raise ValidationError("El cuit ya se ha cargado previamente")



def validate_supplier_name_exists(form, field):
    new_supplier = Suppliers.query.filter_by(name=field.data).first()
    if new_supplier:
        raise ValidationError("El nombre ya existe")


def validate_supplier_phone_exists(form, field):
    new_supplier = Suppliers.query.filter_by(phone=field.data).first()
    if new_supplier:
        raise ValidationError("El teléfono ya existe")


def validate_supplier_cuit_not_exists(form, field):
    new_supplier = Suppliers.query.filter_by(cuit=field.data).first()
    if not new_supplier or new_supplier.hide == 1:
        raise ValidationError("El cuit no existe")

def validate_init_date(form, field):
    initial_date = db.session.query(db.func.min(Sales.date)).first()
    if initial_date[0].strftime('%Y-%m-%d') > str(field.data):
        raise ValidationError("Fecha no valida, ingrese una fecha posterior")

def validate_end_date(form, field):
    end_date = db.session.query(db.func.max(Sales.date)).first()
    if end_date[0].strftime('%Y-%m-%d') < str(field.data):
        raise ValidationError("Fecha no valida, ingrese una fecha anterior")



# PRODUCT ADD

class ProductsFormAdd(FlaskForm):
    code = IntegerField('Código', [DataRequired(), NumberRange(min=0, max=99999999), validate_product_exists])
    description = StringField('Descripción', [DataRequired(), Length(min=2, max=20)])
    supplier = StringField('Proveedor', [DataRequired(), Length(min=2, max=20), check_supplier])
    item_type = StringField('Tipo de prenda', [DataRequired(), Length(min=2, max=20), check_item_type])
    sex = SelectField('Sexo', choices=[('f', 'Femenino'), ('m', 'Masculino')])
    color = StringField('Color', [DataRequired(), Length(min=2, max=20)])
    season = SelectField('Temporada',
                         choices=[('Invierno-Otoño', 'Invierno-Otoño'), ('Verano-Primavera', 'Verano-Primavera')])
    size = SelectField('Talle', choices=[('s', 'S'), ('m', 'M'),('l', 'L'),('xl', 'XL')])
    stock = IntegerField('Stock',[DataRequired(), NumberRange(min=0, max=99999999), LessThanMinStock('min_stock')])
    min_stock = IntegerField('Stock mínimo',[DataRequired(), NumberRange(min=0, max=99999999)])
    price = FloatField('Precio', [DataRequired(),NumberRange(min=0, max=99999999), LessThanCost('cost')])
    cost = FloatField('Costo', [DataRequired(),NumberRange(min=0, max=99999999)])
    submit_add = SubmitField('Agregar producto')


# PRODUCT UPDATE

class ProductsFormUpdate(FlaskForm):
    code = IntegerField('Código', [DataRequired(), NumberRange(min=0), validate_product_not_exists])
    description = StringField('Descripción', [Optional(), Length(min=2, max=20)])
    supplier = StringField('Proveedor', [Optional(), Length(min=2, max=20),check_supplier])
    item_type = StringField('Tipo de prenda', [Optional(), Length(min=2, max=20), check_item_type])
    sex = SelectField('Sexo', choices=[('f', 'Femenino'), ('m', 'Masculino')])
    color = StringField('Color', [Optional(), Length(min=2, max=20)])
    season = SelectField('Temporada',
                         choices=[('Invierno-Otoño', 'Invierno-Otoño'), ('Verano-Primavera', 'Verano-Primavera')])
    size = SelectField('Talle', choices=[('s', 'S'), ('m', 'M'),('l', 'L'),('xl', 'XL')])
    stock = IntegerField('Stock', [Optional(), NumberRange(min=0), LessThanMinStock('min_stock')])
    min_stock = IntegerField('Stock mínimo', [Optional(), NumberRange(min=0)])
    price = FloatField('Precio', [Optional(), NumberRange(min=0), LessThanCost('cost')])
    cost = FloatField('Costo', [Optional(), NumberRange(min=0)])
    submit_update = SubmitField('Editar producto')


# PRODUCT DELETE

class ProductsFormDelete(FlaskForm):
    code = IntegerField('Código', [DataRequired(), NumberRange(min=0), validate_product_not_exists])
    submit_delete = SubmitField('Eliminar producto')


# SUPPLIER ADD

class SuppliersFormAdd(FlaskForm):
    cuit = IntegerField('CUIT', [DataRequired(), NumberRange(min=0), validate_supplier_cuit_exists])
    name = StringField('Nombre', [DataRequired(), Length(min=2, max=20), validate_supplier_name_exists])
    phone = StringField('Teléfono', [DataRequired(), Length(min=2, max=20), validate_supplier_phone_exists])
    submit_add = SubmitField('Agregar proveedor')


# SUPPLIER UPDATE

class SuppliersFormUpdate(FlaskForm):
    cuit = IntegerField('CUIT', [DataRequired(), NumberRange(min=0), validate_supplier_cuit_not_exists])
    name = StringField('Nombre', [Optional(), Length(min=2, max=20)])
    phone = StringField('Teléfono', [Optional(), Length(min=2, max=20)])
    submit_update = SubmitField('Editar proveedor')


# SUPPLIER DELETE

class SuppliersFormDelete(FlaskForm):
    cuit = IntegerField('CUIT', [DataRequired(), NumberRange(min=0), validate_supplier_cuit_not_exists])
    submit_delete = SubmitField('Eliminar proveedor')


class StatisticsForm(FlaskForm):
    product_code = IntegerField('Código del producto',[validate_product_not_exists])
    initial_date = StringField('Fecha de inicio', [DataRequired(), validate_init_date,MoreThanMaxDate('end_date')])
    end_date = StringField('Fecha de fin', [DataRequired(), validate_end_date, validate_init_date,LessThanMinDate('initial_date')])
    options = SelectField('Opciones', choices=[('1','Tipo de Prenda'),('2','Proveedor'), ('3','Sexo'), ('4','Temporada')])
    submit1 = SubmitField('Ventas Diarias')
    submit2 = SubmitField('Cantidad de ventas por')
    submit3 = SubmitField('Ventas Diarias de Producto')
    submit4 = SubmitField('Variación Histórica de Precio de Producto')

# SALE

class SaleInputForm(FlaskForm):
    product_code = IntegerField('Código del producto',[DataRequired(), validate_product_not_exists])
    amount = IntegerField('Cantidad', [DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Ingresar')
    delete = SubmitField('X')
    endSale = SubmitField('Finalizar')