import sys
sys.path.insert(0, '..')

from connection import Connection

connectDb = Connection().connect
cursor = connectDb.cursor()

cursor.execute('''create table public.employees
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')

connectDb.commit()

connectDb.close()
