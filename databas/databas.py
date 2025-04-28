import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Prog2"
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")
