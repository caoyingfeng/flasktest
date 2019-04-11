import pymysql


mysql_conn = pymysql.connect(host="127.0.0.1",
                             port = 3306,
                             user="root",
                             password="199232cyl",
                             charset="utf8",
                             db="test")
c = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from classes where id=1"

res = c.execute(sql)

print(c.fetchall())
c.close()
mysql_conn.close()