import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="första"
)
mycursor = mydb.cursor()
print("Uppkopplad till databasen!")

namn = input("Ange username att söka efter: ")

sql = "SELECT * FROM users WHERE username = %s"
mycursor.execute(sql, (namn,))

resultat = mycursor.fetchall()

if resultat:
    print("Resultat:")
    for rad in resultat:
        print(rad)
else:
    print("Inget username hittades med det namnet.")
