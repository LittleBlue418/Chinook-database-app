import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='littleblue',
                             password='Serendipity2019',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (46, 'Laura')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()
finally:
    connection.close()