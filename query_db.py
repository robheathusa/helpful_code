#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector

cnx = mysql.connector.connect(user='sqladmin', password='password',
                              host='10.0.4.101',
                              database='health')
cursor = cnx.cursor()

query = ("SELECT * FROM vitals ")  # runs a query on the DB and outputs the results


cursor.execute(query)   # executes the query
results = [
    dict(start=row[1], finish=row[2], active_cal=row[3], glucose=row[4], diastolic=row[5],
         systolic=row[6], bpm=row[7], steps=row[8]) for row in cursor.fetchall()
    ]

print('Total Row(s):', cursor.rowcount)

for row in results:
#    print(float('{:.4}'.format((row["active_cal"]))))
    print('{} : {} : {:.4} : {:4} : {:4} : {:4} : {:4} '.format(row["start"], row["finish"],
            float(row["active_cal"]), row["glucose"], row["diastolic"], row["systolic"], row["bpm"]))

cursor.close()
cnx.close()
