#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import csv

# try:
cnx = mysql.connector.connect(user='sqladmin', password='password',
                              host='10.0.4.101',
                              database='health')
cursor = cnx.cursor()

"""
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
"""

add_data = (
    "INSERT INTO vitals (start, finish, active_cal, glucose, diastolic, systolic, bpm, steps) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
)

with open('health_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')  # opens the CSV file for reading
    next(readCSV, None)    # next skips the header row
    for row in readCSV:    # iterates row by row through the file row=iteration
        cursor.execute(add_data, row)    # .execute writes add_data by each row into the DB

# commit the data and close the connection to the database.
cnx.commit()   # commits the changes
cursor.close()   # closes the DB
cnx.close()   # closes the connection
