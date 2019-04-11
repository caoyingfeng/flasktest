from dbpool import POOL
import pymysql


def create_conn():
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def insert(sql, args):
    conn, cursor = create_conn()
    res = cursor.execute(sql,args)
    conn.commit()
    close_conn(conn, cursor)
    return res


def fetch_one(sql,args):
    conn, cursor = create_conn()
    cursor.execute(sql,args)
    res = cursor.fetchone()
    close_conn(conn,cursor)
    return res


def fetch_all(sql,args):
    conn, cursor = create_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res


sql = "insert into classes(id,name) values (%s, %s)"
insert(sql, (2, "李四"))
sql = "select * from classes where name = %s"
print(fetch_one(sql, ("张三")))
