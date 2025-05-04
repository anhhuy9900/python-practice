import json
import logging
import os
import psycopg2
import sys

# rds settings
rds_host = 'localhost'
rds_username = 'postgres'
rds_user_pwd = 'u0wvRxeT44g5jH5WyAw3'
rds_db_name = 'awesome-db'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                    (rds_host, rds_username, rds_user_pwd, rds_db_name)
    conn = psycopg2.connect('postgres://postgres:u0wvRxeT44g5jH5WyAw3@localhost/awesome-db')
except:
    logger.error("ERROR: Could not connect to Postgres instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS Postgres instance succeeded")
def handler(event, context):
    #print('GetAll -handler - event: ', event)
    cur = conn.cursor()
    cur.execute("select * from test")
    results = cur.fetchall()
    json_result = json.dumps(results)
    print(json_result)

    # data = json.loads(event['body'])
    item = {}
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
