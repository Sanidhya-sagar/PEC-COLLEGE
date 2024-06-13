import mysql.connector

con = mysql.connector.connect(
  port=4200,
  host="localhost",
  user="root",
  passwd="mysql")


mycursor = con.cursor()

mycursor.execute("CREATE DATABASE college")

print(con)