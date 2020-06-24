import mysql.connector



mydb = mysql.connector.connect(host='localhost', user='root', password='', database='salon')


mycursor = mydb.cursor()

mycursor.execute('select origin,destination,name  from flights JOIN passengers ON passengers.flight_id=flights.id')

myresult = mycursor.fetchall()
print('Origin     Destination   namr')
if myresult:
    print('Have Records:')joinjoin added
    
    for x in myresult:
       print(x)
    # print('</td></tr></table>')

else:
    print('No Records In Data Base')

str='select origin,destination,name  from flights JOIN passengers ON passengers.flight_id=flights.id WHERE name = "charli "'
mycursor.execute(str)

myresult = mycursor.fetchall()
print('Origin     Destination   name')
if myresult:
    print('Have Records:')
    for x in myresult:
       print(x)
    # print('</td></tr></table>')

else:
    print('No Records In Data Base')
mydb.close()