import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='1234', database='habib')

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM student')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()
