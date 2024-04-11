import mysql.connector

mydb = mysql.connector.connect(
  host="mysqldb",
  user="root",
  password="mysql123",
  database="db_test"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES") #Revisar las tablas existentes
for x in mycursor:
  print(x)
print()

print("Empleados")
mycursor.execute("SELECT * FROM empleado")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

mycursor.close()
mydb.close
