import sys
sys.path.insert(0, '..')

from connection import Connection

connectDb = Connection().connect
cursor = connectDb.cursor()
cursor.execute("update public.employees set department = 'Logistics' where last_name = 'Doe';")

connectDb.commit()
connectDb.close()