from flask import Flask, render_template,request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products,insert_sales,insert_stock,check_available_stock

app = Flask(__name__)

app.secret_key = "codingiseasylike1234"

@app.route('/')
def home():
    x = 5
    name = "Jane"
    numbers = [1,2,3,4,5,6,7,8]

    return render_template('index.html',num = x,name = name,numbers = numbers)

@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data = products_data)


@app.route('/add_product',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = (product_name,buying_price,selling_price)

        insert_products(new_product)
        flash("Product added successfully","success")
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = get_sales()
    products_data = get_products()
    return render_template('sales.html',sales_data = sales_data,products_data = products_data)

@app.route('/add_sale',methods=['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']

        available_stock = check_available_stock(pid)

        if float(quantity) < available_stock:
            print("insufficient stock",'danger')
            return redirect(url_for('sales'))

        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        flash("Sale added successfully","success")
    return redirect(url_for('sales'))

@app.route('/stock')
def stock():
    stock_data = get_stock()
    products_data = get_products()
    return render_template('stock.html',stock_data = stock_data,products_data = products_data)

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['pid']
        Stock_Quantity = request.form['s_quantity']

        new_stock = (product_id,Stock_Quantity)
        insert_stock(new_stock)
        flash("Stock added successfully","success")
    return redirect(url_for('stock'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')


app.run(debug=True)