import psycopg2


def create_table():
    connection = psycopg2.connect("dbname='shop' user='postgres' password='Thebossm@#995' host='localhost' port='5432'")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='shop' user='postgres' password='Thebossm@#995' host='localhost' port='5432'")
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" %(item, quantity, price))
    #cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))    #Alternative method to avoid database injections from hackers
    connection.commit()
    connection.close()


#insert("Coffee cup", 10, 2.5)


# This function deletes a row. pass the row item as an argument
def delete_item(item):
    connection = psycopg2.connect("dbname='shop' user='postgres' password='Thebossm@#995' host='localhost' port='5432'")
    cur = connection.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))    #when there is only one parameter, always end with ','
    connection.commit()
    connection.close()


def view_db():
    connection = psycopg2.connect("dbname='shop' user='postgres' password='Thebossm@#995' host='localhost' port='5432'")
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()                      # .fetchall() methodReturns the rows of a DB as a list of a tuples
    connection.close()
    return rows



def update_db(quantity, price, item):
    connection = psycopg2.connect("dbname='shop' user='postgres' password='Thebossm@#995' host='localhost' port='5432'")
    cur = connection.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    rows = cur.fetchall()                      # .fetchall() methodReturns the rows of a DB as a list of a tuples
    connection.close()
    return rows


create_table()
delete_item("Orange")
print(view_db())