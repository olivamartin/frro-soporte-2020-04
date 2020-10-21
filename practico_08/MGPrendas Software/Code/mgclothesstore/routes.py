from flask import render_template, url_for, flash, redirect, request
from mgclothesstore import app, db
from mgclothesstore.forms import ProductsFormAdd, ProductsFormUpdate, ProductsFormDelete, SuppliersFormAdd, \
    SuppliersFormUpdate, SuppliersFormDelete, StatisticsForm, SaleInputForm
from mgclothesstore.models import db, Suppliers, Seasons, ItemTypes, Sexes, ProductPrices, Products, Sales, Sizes
from datetime import *
import re
from mgclothesstore.statistics_functions import *
from sqlalchemy import and_

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/products", methods=['GET', 'POST'])
def products():
    form_add = ProductsFormAdd()
    form_update = ProductsFormUpdate()
    form_delete = ProductsFormDelete()

    products = Products.query.filter_by(hide=0).all()
    subq = db.session.query(ProductPrices.code, db.func.max(ProductPrices.date).label('maxdate')).group_by(ProductPrices.code).subquery()

    product_prices = db.session.query(ProductPrices.code, ProductPrices.date, ProductPrices.cost, ProductPrices.price).join(subq, and_(ProductPrices.code == subq.c.code,ProductPrices.date == subq.c.maxdate))

    if form_add.submit_add.data and form_add.validate_on_submit():
        supplier = Suppliers.query.filter_by(
            name=re.sub(":|=|¿|¡|}|_|´| |-|!|'|·|#|%|&|/|¨", "", form_add.supplier.data.lower())).first()
        item_type = ItemTypes.query.filter_by(description=form_add.item_type.data).first()
        sex = Sexes.query.filter_by(description=form_add.sex.data).first()
        season = Seasons.query.filter_by(description=form_add.season.data).first()
        size = Sizes.query.filter_by(description=form_add.size.data).first()

        product = Products(code=form_add.code.data,
                           description=form_add.description.data,
                           supplier_id=supplier.cuit,
                           item_type_id=item_type.id,
                           sex_id=sex.id,
                           season_id=season.id,
                           size_id=size.id,
                           color=form_add.color.data,
                           stock=form_add.stock.data,
                           min_stock=form_add.min_stock.data
                           )

        db.session.add(product)

        db.session.commit()

        product_price = ProductPrices(code=form_add.code.data,
                                      date=datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),
                                      cost=form_add.cost.data,
                                      price=form_add.price.data)

        db.session.add(product_price)
        db.session.commit()

        flash('Producto agregado!', 'success')
        return redirect(url_for('products'))

    if form_update.submit_update.data and form_update.validate_on_submit():
        product = Products.query.filter_by(code=form_update.code.data).first()

        if form_update.description.data is not "":
            product.description = form_update.description.data

        if form_update.supplier.data is not "":
            supplier = Suppliers.query.filter_by(name=form_update.supplier.data).first()
            product.supplier_id = supplier.cuit

        if form_update.item_type.data is not "":
            item_type = ItemTypes.query.filter_by(description=form_update.item_type.data).first()
            product.item_type_id = item_type.id

        if form_update.sex.data is not "":
            sex = Sexes.query.filter_by(description=form_update.sex.data).first()
            product.sex_id = sex.id

        if form_update.season.data is not "":
            season = Seasons.query.filter_by(description=form_update.season.data).first()
            product.season_id = season.id

        if form_update.size.data is not "":
            size = Sizes.query.filter_by(description=form_update.size.data).first()
            product.size_id = size.id

        if form_update.color.data is not "":
            product.color = form_update.color.data

        if form_update.stock.data is not None:
            product.stock = form_update.stock.data

        if form_update.min_stock.data is not None:
            product.min_stock = form_update.min_stock.data

        # PRODUCT PRICE
        add_product_price = False

        if form_update.price.data is not None and form_update.cost.data is not None:
            cost = form_update.cost.data
            price = form_update.price.data
            add_product_price = True

        if form_update.cost.data is not None and form_update.price.data is None:
            product_prices = ProductPrices.query.filter_by(code=form_update.code.data).all()
            cost = form_update.cost.data
            price = product_prices[:-1].price
            add_product_price = True

        if form_update.cost.data is None and form_update.price.data is not None:
            product_prices = ProductPrices.query.filter_by(code=form_update.code.data).all()
            cost = product_prices[:-1].cost
            price = form_update.price.data
            add_product_price = True

        if add_product_price:
            product_price = ProductPrices(code=form_update.code.data,
                                          date=datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),
                                          cost=cost,
                                          price=price)
            db.session.add(product_price)

        db.session.commit()

        flash('Producto modificado!', 'success')
        return redirect(url_for('products'))

    if form_delete.submit_delete.data and form_delete.validate_on_submit():
        product = Products.query.filter_by(code=form_delete.code.data).first()
        product.hide = 1
        db.session.commit()

        flash('Producto eliminado!', 'success')
        return redirect(url_for('products'))

    return render_template('products.html', products=products, product_prices=product_prices, form_add=form_add,
                           form_update=form_update, form_delete=form_delete)


@app.route("/suppliers", methods=['GET', 'POST'])
def suppliers():
    form_add = SuppliersFormAdd()
    form_update = SuppliersFormUpdate()
    form_delete = SuppliersFormDelete()

    suppliers = Suppliers.query.filter_by(hide=0).all()

    if form_add.submit_add.data and form_add.validate_on_submit():
        supplier = Suppliers(cuit=form_add.cuit.data,
                             name=form_add.name.data,
                             phone=form_add.phone.data
                             )

        db.session.add(supplier)
        db.session.commit()
        flash('Proveedor agregado!', 'success')
        return redirect(url_for('suppliers'))

    if form_update.submit_update.data and form_update.validate_on_submit():
        supplier = Suppliers.query.filter_by(cuit=form_update.cuit.data).first()

        if supplier.name is not None:
            supplier.name = form_update.name.data

        if supplier.phone is not None:
            supplier.phone = form_update.phone.data

        db.session.commit()

        flash('Proveedor modificado!', 'success')
        return redirect(url_for('suppliers'))

    if form_delete.submit_delete.data and form_delete.validate_on_submit():
        supplier = Suppliers.query.filter_by(cuit=form_delete.cuit.data).first()
        supplier.hide = 1
        db.session.commit()

        flash('Proveedor eliminado!', 'success')
        return redirect(url_for('suppliers'))

    return render_template('suppliers.html', suppliers=suppliers, form_add=form_add, form_update=form_update,
                           form_delete=form_delete)


@app.route("/statistics", methods=['GET', 'POST'])
def statistics():
    form_statistics = StatisticsForm()
    
    plot = ''

    if form_statistics.submit1.data and form_statistics.validate_on_submit():
        plot1(form_statistics.initial_date.data, form_statistics.end_date.data)
        plot = 'plot1.png'

    if form_statistics.submit2.data and form_statistics.validate_on_submit():
        if form_statistics.options.data == '1': plot2_1()
        if form_statistics.options.data == '2': plot2_2()
        if form_statistics.options.data == '3': plot2_3()
        if form_statistics.options.data == '4': plot2_4()
        plot = 'plot2.png'

    if form_statistics.submit3.data and form_statistics.validate_on_submit():
        plot3(form_statistics.initial_date.data, form_statistics.end_date.data, form_statistics.product_code.data)
        plot = 'plot3.png'

    if form_statistics.submit4.data and form_statistics.validate_on_submit():
        plot4(form_statistics.initial_date.data, form_statistics.end_date.data, form_statistics.product_code.data)
        plot = 'plot4.png'

    return render_template('statistics.html', form_statistics=form_statistics, show_modal=True, plot=plot)

shopping_cart = []
total = 0
@app.route("/sales", methods=['GET', 'POST'])
def sales():
    global shopping_cart
    global total
    
    form_sales = SaleInputForm()

    if form_sales.submit.data and form_sales.validate_on_submit():
        product = Products.query.filter_by(code=form_sales.product_code.data).first()
        if product.stock >= form_sales.amount.data:
            
            price = db.session.query(ProductPrices.code, db.func.max(ProductPrices.date), ProductPrices.price).group_by(ProductPrices.code).filter(ProductPrices.code == product.code).all()[0][2]
            
            subtotal = price * form_sales.amount.data
            
            shopping_cart.append({
                'position': len(shopping_cart),
                'product_code': product.code,
                'description': product.description,
                'price': price,
                'amount': form_sales.amount.data,
                'subtotal': subtotal
                })
            total += subtotal
        else:
            flash('No hay stock suficiente','danger')
    
    if form_sales.endSale.data and form_sales.validate_on_submit():
        for item in shopping_cart:
            sale = Sales(date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S'), 
                        product_id = item['product_code'],
                        amount = item['amount'])
            db.session.add(sale)
        db.session.commit()
        shopping_cart = []
        total = 0
        flash('Vendido!', 'success')

    # Remove item from shopping cart
    position = request.args.get('id')
    if position is not None:
        for index, item in enumerate(shopping_cart):
            if item['position'] == int(position):
                shopping_cart.pop(index)
                total -= item['subtotal']
                
        
        
    return render_template('sales.html', form_sales=form_sales, shopping_cart=shopping_cart, total=total)