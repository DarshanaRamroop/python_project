import mysql.connector
def get_connection():
    con = mysql.connector.connect(host="localhost", user="venus", password="tsarzeus7&",
    db="bomarseboutikdb")
    cur = con.cursor()
    return cur, con