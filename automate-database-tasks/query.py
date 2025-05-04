import sys

sys.path.insert(0, '..')

import psycopg2
from psycopg2.extras import RealDictCursor
from connection import Connection

connectDb = Connection().connect
cursor = connectDb.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor.execute("select * from public.employees where salary < 50000;")
# cursor.execute("select * from public.employees where last_name like '%Richard%';")
# cursor.execute("select * from public.employees where salary between 40000 and 45000;")
# cursor.execute("select * from public.employees where department in ('Sales', 'IT');")

# Fetching all the rows in a query result; returns a list
# records = cursor.fetchall()
# print('QUERY RECORDS : ', records)
# for record in records:
#     print(f"{(record['id'])}")

# Fetching the next row in a query result; returns a tuple; returns None when no more records are available
record = cursor.fetchone()
print('QUERY RECORDS : ', record)
print("id : {}, last_name = {}, first_name = {}".format(record['id'], record['first_name'], record['last_name']))
