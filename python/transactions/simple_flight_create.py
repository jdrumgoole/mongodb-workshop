
import pymongo
from transactions.flight import Flight

if __name__ == "__main__" :

    client = pymongo.MongoClient()
    database = client[ "TEST_TXN"]

    # make a flight with 70 rows, 6 seats per row
    EI_179 
    EI_179 = Flight( database, "EI179", 70, ["A", "B", "C", "D", "E", "F"])