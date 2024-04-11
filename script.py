import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql123",
  database="test1",
  port="3310"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES") #Revisar las tablas existentes
for x in mycursor:
  print(x)
print()

print("Empleados")
mycursor.execute("SELECT * FROM Empleado")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

print()

print("Clientes")
mycursor.execute("SELECT * FROM Cliente")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)


mycursor.close()
mydb.close
