#!/usr/bin/env python3
from flask import Flask, render_template
# from dbc import connection
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(user='sqladmin', password='password',
                              host='10.0.4.101',
                              database='health')

# cnx = connection()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/query/', methods=["GET"])
def query_page():

    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM vitals")

    results = [dict(start=row[1], finish=row[2], active_cal=row[3], glucose=row[4], diastolic=row[5], systolic=row[6], bpm=row[7], steps=row[8]) for row in cursor.fetchall()]

    return render_template('show_results.html', results=results)


"""
    for row in cursor.fetchall():
        results = [dict(start=row[0], finish=row[1], active_cal=row[2])]


    return render_template('show_results.html', results=results)

"""


if __name__ == '__main__':
    app.run(debug=True)
