from sql_connection_decorator import mysql_connection, pymssql_connection


@mysql_connection
def mysql_query(cursor):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    cursor.execute(sql, val)
    cursor.commit()

    cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
    # print(cursor.fetchall())
    # print(cursor.fetchone())


@pymssql_connection
def mssql_query(cursor):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    cursor.execute(sql, val)
    cursor.commit()

    cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
    # print(cursor.fetchall())
    # print(cursor.fetchone())
    for row in cursor:
        print('row = %r' % (row,))


if __name__ == '__main__':
    mysql_query()
    mssql_query()
