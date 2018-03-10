
import pymongo
import random
import datetime
import time
from argparse import ArgumentParser

def send_data( count, collection, sensor_name ) :

    temp = random.uniform( -20, 2000 )
    print( "Writing temp : %f" % ( temp ))

    collection.insert( { "temp"  : temp,
                         "name"  : sensor_name,
                         "count" : count,
                         "ts"    : datetime.datetime.utcnow()})


if __name__ == "__main__" :

    parser = ArgumentParser()

    parser.add_argument( "--host", default="mongodb://localhost:27017" )
    parser.add_argument( "--sensor_name", default="manifold sensor")
    parser.add_argument( "--drop", default=False )

    args = parser.parse_args()
    client = pymongo.MongoClient( host= args.host )

    db = client[ "IOTDB"] ;

    if args.drop :
        db.drop_collection( "sensor_data")
        print( "Dropping collection sensor_data")

    collection = db[ "sensor_data"]


    count = 0
    while True :
        count = count + 1
        wait_time = random.uniform(0.0, 0.1)
        time.sleep(wait_time)
        send_data( count, collection, args.sensor_name )

