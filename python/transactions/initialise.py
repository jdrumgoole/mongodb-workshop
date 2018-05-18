import pymongo

if __name__ == "__main__" :

    client = pymongo.MongoClient()
    database = client[ "AIRLINE"]
    seat_log = database[ "seats"]
    payment_log == database[ "payments"]
