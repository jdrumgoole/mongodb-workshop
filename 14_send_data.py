
import pymongo
import random
import datetime
import time
from argparse import ArgumentParser
from multiprocessing import Process


def send_data( count, collection, sensor_name ) :


    temp = random.uniform( -20, 2000 )
    if args.verbose:
        print( "Writing temp : %f for sensor %s" % ( temp, sensor_name ))

    collection.insert( { "temp"  : temp,
                         "name"  : sensor_name,
                         "count" : count,
                         "ts"    : datetime.datetime.utcnow()})


def send_loop( sensor_name ) :

    client = pymongo.MongoClient( host= args.host )
    db = client[ "IOTDB"]
    collection = db[ "sensor_data"]

    count = 0
    while True :
        count = count + 1
        wait_time = random.uniform(0.0, 0.01)
        time.sleep(wait_time)
        send_data( count, collection, sensor_name )


if __name__ == "__main__" :

    parser = ArgumentParser()

    parser.add_argument( "--host", default="mongodb://localhost:27017" )
    parser.add_argument( "--sensor_name", default="manifold sensor")
    parser.add_argument( "--procs", default=1, type=int )
    parser.add_argument( "--verbose", default=False )

    args = parser.parse_args()

    procs = []

    for i in range( args.procs ):
        proc = Process(target=send_loop, name="process" + "_" + str( i),
                       args=( args.sensor_name + "_" + str( i ), ))
        procs.append(proc)
        print( "Staring : %s" % proc.name )
        proc.start()

    try :
        while True:
            time.sleep( 0.1 )
    except KeyboardInterrupt :
        for i in procs:
            print( "terminating: %s" % i.name )
            i.terminate()

    for proc in procs:
        proc.join()


