import numpy as np
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta

"""
Statistics Package
"""

plt.rcParams['figure.figsize'] = (16,5)
colors=["rebeccapurple", "darkcyan", "deepskyblue", "olivedrab", "forestgreen", "darkkhaki", 
        "darkgoldenrod", "saddlebrown", "firebrick", "deeppink", "navy", "dimgray", "salmon"]

###################################################

def setup_df(initial_date=None, final_date=None):
    engine = sqlalchemy.create_engine("mysql://root:root@localhost/mgclothesstore")

    df_products = pd.read_sql_table("products", engine, index_col='code')
    df_item_types = pd.read_sql_table("item_types", engine)
    df_product_prices = pd.read_sql_table("product_prices", engine, index_col='date')
    df_suppliers = pd.read_sql_table("suppliers", engine)
    df_seasons = pd.read_sql_table("seasons", engine, index_col='id')
    df_sex = pd.read_sql_table("sexes", engine, index_col='id')

    df_sales = pd.read_sql_table("sales", engine, index_col='date')
    
    if initial_date != None and final_date != None:
        mask = (df_sales.index > initial_date) & (df_sales.index <= final_date)
        df_sales = df_sales.iloc[mask]

    return df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex

###################################################

def plot1(initial_date, final_date):
    initial_date = pd.Timestamp(initial_date)
    final_date = pd.Timestamp(final_date) + timedelta(days=1)

    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df(initial_date, final_date)

    resampled = df_sales.resample('1D').sum()
    idx = resampled.index
    data = resampled['amount']

    sns.lineplot(idx, data, color='rebeccapurple', drawstyle='steps-pre')

    plt.xlabel('Días', fontsize=13)
    plt.ylabel('Cantidad de Ventas', fontsize=13)
    plt.xlim(idx[0], idx[-1])
    plt.ylim(np.nanmin(data[1:]-1), np.nanmax(data+1))
    plt.title(f'Ventas Diarias desde {idx[0].day}/{idx[0].month}/{idx[0].year} hasta {idx[-1].day}/{idx[-1].month}/{idx[-1].year}', fontsize=20)
    plt.tight_layout()
    plt.savefig('mgclothesstore/static/images/plots/plot1.png')
    plt.close()

###################################################

def barplots(df_sales, df_products, target_df, lefton, righton, column, x_labels, palette, title):
    merge_sales_product = df_sales.merge(df_products, how='inner', left_on='product_id', right_on='code')
    merge_product_target = merge_sales_product.merge(target_df, how='right', left_on=lefton, right_on=righton)[column].value_counts()
    
    merge_product_target = merge_product_target.to_frame()
    merge_product_target.reset_index(inplace=True)
    merge_product_target['index'] = merge_product_target['index'].str.capitalize()

    sns.barplot(x='index', y=column, data=merge_product_target, palette=palette)
    
    plt.title(title, fontsize=20)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('mgclothesstore/static/images/plots/plot2.png')
    plt.close()

def plot2_1():
    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df()
    barplots(df_sales, df_products, df_item_types, lefton='item_type_id', righton='id', column='description_y', x_labels='description', palette='Paired', title='Cantidad vendida por tipo de prenda')

def plot2_2():
    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df()
    barplots(df_sales, df_products, df_suppliers, lefton='supplier_id', righton='cuit', column='name', x_labels='name', palette='Set2', title='Cantidad vendida por proveedor')

def plot2_3():
    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df()
    barplots(df_sales, df_products, df_sex, lefton='sex_id', righton='id', column='description_y', x_labels='description', palette='PuBu', title='Cantidad vendida por sexo')

def plot2_4():
    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df()
    barplots(df_sales, df_products, df_seasons, lefton='season_id', righton='id', column='description_y', x_labels='description', palette='coolwarm', title='Cantidad vendida por temporada')

###################################################

def plot3(initial_date, final_date, product_code):
    initial_date = pd.Timestamp(initial_date)
    final_date = pd.Timestamp(final_date) + timedelta(days=1)

    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df(initial_date, final_date)

    product_description = df_products[df_products.index == product_code]['description'].to_numpy()[0]

    df_sales_product = df_sales[df_sales['product_id'] == product_code]
    resampled = df_sales_product.resample('1D', closed="right").min()
    idx = resampled.index

    data = np.diff(resampled['id'], prepend=True)
    sns.lineplot(idx, data, color='rebeccapurple', drawstyle='steps-pre')

    plt.xlabel('Días', fontsize=13)
    plt.ylabel('Cantidad de Ventas', fontsize=13)
    plt.xlim(idx[0], idx[-1])
    plt.ylim(0, np.nanmax(data)+1)
    plt.title(f'Ventas Diarias de {product_description} desde {idx[0].day}/{idx[0].month}/{idx[0].year} hasta {idx[-1].day}/{idx[-1].month}/{idx[-1].year}', fontsize=20)
    plt.tight_layout()
    plt.savefig('mgclothesstore/static/images/plots/plot3.png')
    plt.close()

###################################################

def plot4(initial_date, final_date, product_code):
    initial_date = pd.Timestamp(initial_date)
    final_date = pd.Timestamp(final_date)

    df_products, df_item_types, df_product_prices, df_sales, df_suppliers, df_seasons, df_sex = setup_df(initial_date, final_date)
    
    product_description = df_products[df_products.index == product_code]['description'].to_numpy()[0]

    product_price = df_product_prices[df_product_prices['code'] == product_code]

    plt.plot(product_price['price'], label='Precio')
    plt.plot(product_price['cost'], label='Costo')

    idx = product_price.index

    plt.xlabel('Días', fontsize=13)
    plt.ylabel('Monto $', fontsize=13)
    plt.xlim(idx[0], idx[-1])
    plt.title(f'Precio y costo de {product_description} desde {idx[0].day}/{idx[0].month}/{idx[0].year} hasta {idx[-1].day}/{idx[-1].month}/{idx[-1].year}', fontsize=20)
    plt.tight_layout()
    plt.savefig('mgclothesstore/static/images/plots/plot4.png')
    plt.close()