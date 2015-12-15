#!/usr/bin/python

import pyodbc
import json
import datetime
import requests
import time

def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__

def query_db(query, cnx):
    conn = pyodbc.connect(cnx)
    cur = conn.cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return r

my_query = query_db("SHOW TABLE STATUS FROM mysql", \
"DRIVER={MySQL};SERVER=localhost;DATABASE=mysql;PWD=password")

json_output = json.dumps(my_query, ensure_ascii=False, default=json_default).encode('utf-32-le')

#print json_output
r = requests.post('http://requestb.in/qyy05lqy', json_output)
print r.status_code
print r.content
