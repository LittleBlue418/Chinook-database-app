import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='littleblue',
                             password='Serendipity2019',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
        connection.commit()
finally:
    connection.close()