import psycopg2

#establishing a db connection
conn = psycopg2.connect(host="localhost",port=5432,user="postgres", password="2691" ,dbname="flask_myduka")

#creating a cursor object to perform db operations
cur = conn.cursor()

#cur.execute('Select * from products')
#products = cur.fetchall()
#print(products)

def get_products():
    cur.execute('Select * from products')
    products = cur.fetchall() # products in fuction is local
    return products



def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('shoes',2000,2500)")
    conn.commit()

insert_products()

products = get_products()   # products outside function is global
print(products)


