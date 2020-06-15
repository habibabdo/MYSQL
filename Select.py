import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='1234', database='salon')

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM contacts')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()
