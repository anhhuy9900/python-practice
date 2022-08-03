import sys
sys.path.insert(0, '..')

from connection import Connection

connectDb = Connection().connect
cursor = connectDb.cursor()
cursor.execute("delete from public.employees where salary > 50000;")

connectDb.commit()
connectDb.close()