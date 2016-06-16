#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from dbcon import connection
import mysql.connector
import matplotlib.pyplot as plt

cnx = mysql.connector.connect(user='sqladmin', password='password',
                              host='10.0.4.101',
                              database='health')
# cnx = connection()

cursor = cnx.cursor()

query = ("SELECT * FROM vitals ")  # runs a query on the DB and outputs the results

cursor.execute(query)   # executes the query
result = cursor.fetchall()  # return the query to result

def numlist():
    x = []
    y = []
    for record in result:
        x.append(record[0])
        y.append(record[7])
    plt.plot(x, y, 'ko')
    # plt.axis([min(t), max(t), min(s), max(s)])
    plt.title('BPM')
    plt.xlabel('Time')
    plt.ylabel('Active Calories')
    plt.grid(True)
    plt.show()

numlist()

cursor.close()
