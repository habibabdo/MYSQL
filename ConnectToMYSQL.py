import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='habib', passwd='', database='salon')

print(mydb)

#mydb.close()
