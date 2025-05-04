from pymongo import MongoClient
import json
import simplejson

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost:27017/practice"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['practice']

def insert_zips_to_db():
   dbname = get_database()
   with open("zips.json") as fp:
    json_lines = fp.readlines()
    fp.close()
    for json_line in json_lines:
        dbname['zips'].insert_one(json.loads(json_line))

# Return States with Populations above 10 Million
def get_total_pop(dbname):
   pipeline = [
      {
         "$group": {
            "_id": "$state",
            "totalPop": {
               "$sum": "$pop"
            }
         }
      },
      { "$match": { "totalPop": { "$gte": 10*1e6 } } }
   ]
   cursor = dbname['zips'].aggregate(pipeline)
   print(json.dumps(list(cursor), indent=2))

# Return Average City Population by State
def get_average_city(dbname):
   pipeline = [
      { "$group": {"_id": {"state": "$state", "city": "$city" }, "city_pop": { "$sum": "$pop" } } }, 
      { "$group": { "_id": "$_id.state", "avgCityPop": { "$avg": "$city_pop" } } },
      { "$sort": {"avgCityPop": -1}},
      { "$limit": 10}
   ]
   cursor = dbname['zips'].aggregate(pipeline)
   print(json.dumps(list(cursor), indent=2))
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   # print(dbname)
   #  insert_zips_to_db()
   # get_total_pop(dbname)

   get_average_city(dbname)