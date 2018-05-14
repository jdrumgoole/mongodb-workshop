
import pymongo
from argparse import ArgumentParser
import pprint

if __name__ == "__main__" :

    parser = ArgumentParser()

    parser.add_argument( "--host", default="mongodb://localhost:27017", help="mongodb URI for connecting to server")
    parser.add_argument( "--watch", default="test.test", help="Watch <database.colection")

    args = parser.parse_args()

    client = pymongo.MongoClient( host=args.host)

    ( database_name, dot, collection_name ) = args.watch.partition( ".")

    database = client[database_name]
    collection = database[collection_name]

    watch_cursor = collection.watch()

    print( "Watching: {}".format(args.watch))
    for d in watch_cursor:
        pprint.pprint(d)
