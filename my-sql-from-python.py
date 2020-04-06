import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             user='littleblue',
                             password='Serendipity2019',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_names = ['Bob', 'Laura']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({})".format(format_strings), list_of_names)
        connection.commit()
finally:
    connection.close()