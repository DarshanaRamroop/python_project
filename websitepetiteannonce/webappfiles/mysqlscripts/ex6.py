import mysql.connector
import dbconnect
cur, con = dbconnect.get_connection()
cur.execute("CREATE TABLE tbllanguage ("
"language_id INTEGER PRIMARY KEY AUTO_INCREMENT,"
"language_code VARCHAR(8) NOT NULL,"
"language_name VARCHAR(50) NOT NULL )")