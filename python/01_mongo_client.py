import pymongo
"""
Before running this program download mongodb from

https://www.mongodb.com/download-center#community

run the mongod deemon to start a database server.
This will start a server on port 27017.
This client connects to that port by default.

See also

http://api.mongodb.com/python/current/api/pymongo/mongo_client.html

@author: jdrumgoole
"""

import pprint
import pymongo
from argparse import ArgumentParser

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument( "--host")
    args = parser.parse_args()

    if not args.host:
        args.host = "mongodb://localhost:27017"

    client = pymongo.MongoClient( host=args.host)
    database = client["test"]
    response = database.command("ismaster")
    pprint.pprint(response)