"""
There are five important steps to take when working with Databases, namely:
1. Creating the connection using the sqlite3 library.
2. Creating the cursor
3  Executing an SQL - using the .execute method to pass a command to the db
4. Commit Method
5. Close the connection

"""
import sqlite3


def create_table():
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()


# insert("Coffee cup", 10, 2.5)


# This function deletes a row. pass the row item as an argument
def delete_item(item):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))  # when there is only one parameter, always end with ','
    connection.commit()
    connection.close()


def view_db():
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()  # .fetchall() methodReturns the rows of a DB as a list of a tuples
    connection.close()
    return rows


def update_db(quantity, price, item):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    rows = cur.fetchall()  # .fetchall() methodReturns the rows of a DB as a list of a tuples
    connection.close()
    return rows


delete_item("Wine Glass")
print(view_db())
