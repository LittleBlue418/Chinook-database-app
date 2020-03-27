import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='littleblue',
                             password='Serendipity2019',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    connection.close()