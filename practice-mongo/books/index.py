from pymongo import MongoClient
import json

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost:27017/practice"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['practice']

def insert_books_to_db():
   dbname = get_database()
   with open("./books.json") as fp:
    json_lines = fp.readlines()
    fp.close()
    #dbname['books'].insert_many(json.dumps(json_lines))  
    for json_line in json_lines:
        dbname['books'].insert_one(json.loads(json_line))     

  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   # print(dbname)
   insert_books_to_db()