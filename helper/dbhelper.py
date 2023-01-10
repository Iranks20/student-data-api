# from flask import request, jsonify
# from config import DB_CONFIG as conf
# from application import mysql


# class Database:
#     def __init__(self):
#         self.conn = mysql.connection.cursor()

    
#     def select(self, query):
#         self.conn.execute(query)
#         rows = self.conn.fetchall()
#         return rows

    
#     def delete(self, query):
#         self.conn.execute(query)
#         mysql.connection.commit()
#         self.conn.close()
#         return True

    
#     def insert(self, table_name, **data):
#         keys = ', '.join(['%s'] * len(data))
#         columns = ', '.join(data.keys())
#         values = tuple(data.values())
#         sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table_name, columns, keys)
#         self.conn.execute(sql, values)
#         mysql.connection.commit()
#         self.conn.close()
#         last_id = self.conn.lastrowid
#         return last_id

    
#     def Update(self, table, where, **d):
#         sql = 'UPDATE ' + table + ' SET {}'.format(', '.join('{}=%s'.format(k) for k in d))
#         sql = sql + ' WHERE ' + where
#         write_to_file(sql)
#         values = tuple(d.values())
#         self.conn.execute(sql, values)
#         mysql.connection.commit()
#         self.conn.close()
#         last_id = self.conn.lastrowid
#         return last_id


# def write_to_file(data):
#     f = open("output.txt", "w")
#     f.write(data)
#     f.close()

# python mysql connector version


# from config import DB_CONFIG as conf
# from flask import request, jsonify
# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='student_data',
#                                          user='root',
#                                          password='')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")


#                         ******************************PYTHON MYSQL CONNECTOR VERSION *********************************

from flask import jsonify
import mysql.connector
from config import DB_CONFIG as conf
from application import mysql

class Database:
    def __init__(self):
        self.conn = mysql.connection.cursor(dictionary=True)

    
    def insert(self, table, **data):
        keys = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, keys)
        self.conn.execute(sql, values)
        mysql.connection.commit()
        self.conn.close()
        last_id = self.conn.lastrowid
        return last_id


    def select(self, query):
        self.conn.execute(query)
        rows = self.conn.fetchall()
        return rows

    
    def Update(self, table, where, **d):
        sql = 'UPDATE ' + table + ' SET {}'.format(', '.join('{}=%s'.format(k) for k in d))
        sql = sql + ' WHERE ' + where
        write_to_file(sql)
        values = tuple(d.values())
        self.conn.execute(sql, values)
        mysql.connection.commit()
        self.conn.close()
        last_id = self.conn.lastrowid
        return last_id

    def delete(self, query):
        self.conn.execute(query)
        mysql.connection.commit()
        self.conn.close()
        return True



def write_to_file(data):
    f = open("output.txt", "w")
    f.write(data)
    f.close()