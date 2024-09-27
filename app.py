import mysql.connector

def connect():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Lungan@7@7',
            database='ecommerce'
        )

        print('Database connected')
        return conn 
    
    except mysql.connector.Error as error:
        print(f'Connection failed: {error}')
        return None 

def add(name, description, price, stock_quantity, category):

    db = connect() 
    if db is None:
        return
    
    cursor = db.cursor() 
    sql = 'INSERT INTO products (name, description, price, stock_quantity, category) VALUES (%s, %s, %s, %s, %s)'
    
    values = (name, description, price, stock_quantity, category)
    
    try:
        cursor.execute(sql, values) 
        db.commit() 
    except mysql.connector.Error as error:
        print(f'Error executing query: {error}')
    finally:
        cursor.close() 
        db.close() 

def getProductById(id):
    db = connect() 
    if db is None:
        return
    
    cursor = db.cursor()
    sql = 'SELECT * FROM products WHERE ID = %s'
    id = (id, )

    try:
        cursor.execute(sql, id)
        data = cursor.fetchone()
        print(data)

    except mysql.connector.Error as error:
        print(f'Error executing query: {error}')

    finally:
        cursor.close() 
        db.close() 
    
def update(id, name, description, price, stock_quantity, category):
    db = connect() 
    if db is None:
        return
    
    cursor = db.cursor()
    sql = 'UPDATE products SET name = %s, description = %s, price = %s, stock_quantity= %s, category = %s WHERE ID = %s'

    values = (name, description, price, stock_quantity, category, id)

    try:
        cursor.execute(sql, values)
        db.commit()

    except mysql.connector.Error as error:
        print(f'Error executing query: {error}')

    finally:
        cursor.close() 
        db.close() 

def delete(id):
    db = connect() 

    if db is None:
        return
    
    cursor = db.cursor()
    sql = 'DELETE FROM products WHERE ID = %s'

    id = (id,)

    try:
        cursor.execute(sql, id)
        db.commit()
        print(f'field with {id} id  deleted')

    except mysql.connector.Error as error:
        print(f'Error executing query: {error}')

    finally:
        cursor.close() 
        db.close()

def getProductByCategory(category):
    db = connect() 
    if db is None:
        return
    
    cursor = db.cursor()
    sql = 'SELECT * FROM products WHERE category = %s'
    category = (category, )

    try:
        cursor.execute(sql, category)
        data = cursor.fetchall()
        
        for i in data:
            print(i)

    except mysql.connector.Error as error:
        print(f'Error executing query: {error}')

    finally:
        cursor.close() 
        db.close() 

def getRangeProduct(min, max):
    db = connect() 
    if db is None:
        return
    
    cursor = db.cursor()
    sql = 'SELECT * FROM products WHERE Price > %s AND Price < %s'

    category = (min, max )

    try:
        cursor.execute(sql, category)
        data = cursor.fetchall()
        
        for i in data:
            print(i)

    except mysql.connector.Error as error:
        print(f'Error executing query: {error}')

    finally:
        cursor.close() 
        db.close()
    
def main():
    while True:
        try:
            menu = int(input('Menu: \n1. ADD \n2. Get product by Id \n3. Update \n4. Delete \n5. Get product by category \n6. Get product in a price range \n0. To Exit \n>'))

            if menu == 0:
                break

            if menu == 1:

                name = input('Enter product name: ')
                des = input('Enter product description: ')
                price = float(input('Enter product price: '))
                quantity = int(input('Enter product quantity: '))
                category = input('Enter product category: ')

                add(name, des, price, quantity, category)
            
            elif menu == 2:

                id = int(input('Enter product Id: '))
                getProductById(id)
            
            elif menu == 3:

                id = int(input('Enter product Id: '))
                name = input('Enter product name: ')
                des = input('Enter product description: ')
                price = float(input('Enter product price: '))
                quantity = int(input('Enter product quantity: '))
                category = input('Enter product category: ')

                update(id, name, des, price, quantity, category)
            
            elif menu == 4:
                id = int(input('Enter product Id: '))
                delete(id)
            
            elif menu == 5:
                category = input('Enter product category: ')
                getProductByCategory(category)
            
            elif menu == 6:
                min = float(input('Enter minimun price: '))
                max = float(input('Enter maximum price: '))

                getRangeProduct(min, max)
        
        except ValueError:
            print(f'Enter a valid value: {ValueError}')

if __name__ == '__main__':
    main()