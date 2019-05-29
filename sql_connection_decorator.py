import mysql.connector
from mysql.connector import errorcode
import pymssql
import _mssql


def mysql_connection(f):
    def with_connection_(*args, **kwargs):
        # or use a pool, or a factory function...

        conn = mysql.connector.connect(
            host='',
            user='',
            passwd='',
            database=''
        )

        func = None

        try:
            func = f(conn.cursor(), *args, **kwargs)

            return func
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            conn.rollback()
        finally:
            conn.commit()
            conn.close()

        return func

    return with_connection_


def pymssql_connection(f):
    def with_connection_(*args, **kwargs):
        try:
            with pymssql.connect('host', 'user', 'pwd', 'db') as conn:
                with conn.cursor() as cursor:  # conn.cursor(as_dict=True)
                    func = f(cursor(), *args, **kwargs)

                    return func

        except _mssql.MssqlDatabaseException as e:
            print("A MSSQLDatabaseException has been caught.")
            print('Number = ', e.number)
            print('Severity = ', e.severity)
            print('State = ', e.state)
            print('Message = ', e.message)
            conn.rollback()
        finally:
            conn.commit()
            conn.close()

        return func

    return with_connection_
