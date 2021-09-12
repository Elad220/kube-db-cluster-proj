import mysql.connector
import socket
sql_pod_ip = "172.17.0.3"
with open('/app/add_to_book.txt') as file:
       #line = file.read()
    lines = file.readlines()
records = [line.split() for line in lines]
mydb = mysql.connector.connect(
    host=sql_pod_ip,
    user="",
    password="password",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS addressBook")
mycursor.close()
mydb.close()
mydb = mysql.connector.connect(
    host=sql_pod_ip,
    user="",
    password="password",
    database="addressBook"
)
mycursor = mydb.cursor()
create_addressBook_query = """
    CREATE TABLE IF NOT EXISTS addressBook(
        id VARCHAR(10), first_name VARCHAR(20), second_name VARCHAR(20), address VARCHAR(40))
    """
mycursor.execute(create_addressBook_query)
mydb.commit()
insert_query = """INSERT INTO addressBook (ID, first_name, second_name, address) VALUES ( %s, %s, %s, %s )"""
mycursor.executemany(insert_query, records)
mydb.commit()
mycursor.close()
mydb.close()
