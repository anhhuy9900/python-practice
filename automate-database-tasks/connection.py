import psycopg2


class Connection:
    connect = None;

    def __init__(self):
        try:
            self.connect = psycopg2.connect(database="db_test", user="postgres", password="postgres", host="localhost", port="5432")
        except psycopg2.Error as err:
            print("An error was generated")
        else:
            print("Connection to database was successful!")

