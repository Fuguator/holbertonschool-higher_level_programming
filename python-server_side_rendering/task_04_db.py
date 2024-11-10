from flask import Flask, render_template, request
from json import load
import csv
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as file:
        items = load(file).get('items') or []

    return render_template('items.html', items=items)

def read_json(file_path):
    with open(file_path) as file:
        return load(file)
    
def read_csv(file_path):
    products = []
    with open(file_path) as file:
        datas = csv.DictReader(file)
        for data in datas:
            data['id'] = int(data['id'])
            data['price'] = float(data['price'])
            products.append(data)
    return products

def sqlite_reader():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        products.append(product)
    print(products)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    products = []

    if source == 'csv':
        file_path = 'products.csv'
        if os.path.exists(file_path):
            products = read_csv(file_path)
        else:
            return render_template('product_display.html', error='File not exists')
    elif source == 'json':
        file_path = 'products.json'
        if os.path.exists(file_path):
            products = read_json(file_path)
        else:
            return render_template('product_display.html', error='File not exists')
    elif source == 'sql':
        products = sqlite_reader()
    else:
        return render_template('product_display.html', error="Wrong source")

    if id:
        id = int(id)
        products = [product for product in products if product['id'] == id]
        if not products:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
