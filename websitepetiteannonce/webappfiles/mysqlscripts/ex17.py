import mysql.connector
import dbconnect
cur, con = dbconnect.get_connection()
sql = "SELECT * FROM tblgenre WHERE genre LIKE '%t%'"
cur.execute(sql)
myresult = cur.fetchall()
for x in myresult:
    print(x)
