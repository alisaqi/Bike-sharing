import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# def config(user,password,host):
#     user = (user)
#     password = (password)
#     host = (host)
#
#     return host,password,user

dbName = 'MIS'
def connect():
    con = psycopg2.connect(
        user='postgres',
        password='ali',
        host='localhost'
    )

    cursor = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    return cursor, con


def CreateDB(cursor, con, database_name):
    global dbName
    dbName =  database_name
    sql = "create database " + dbName + ";"
    try:
        cursor.execute(sql)
        con.commit()
        print("database " + dbName + " is created")
        cursor.close()
        con.close()

        return dbName
    except:
        print("this db is already created")
        return dbName


def connect_to_DB(name):
    con = psycopg2.connect(dbname=str(name), user='postgres', password='ali')
    cursor = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    return cursor, con




# def data():

#
# cursor,con = connect()
# CreateDB(cursor,con)
