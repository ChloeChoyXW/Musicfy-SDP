import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mysql#Pa55",
    database = "musicfy_db"
)

mycursor = db.cursor()

a = mycursor.execute("select * from user_tbl")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)