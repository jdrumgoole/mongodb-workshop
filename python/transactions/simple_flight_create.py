import pymongo
from transactions.flight import Seat_Log
from transactions.flight import Person
from transactions.payment import Payment_Log

if __name__ == "__main__":
    client = pymongo.MongoClient()
    database = client["TEST_TXN"]
    seat_log_collection = database["seat_log"]
    payment_log_collection = database[ "payment_log"]

    # make a flight with 70 rows, 6 seats per row
    seats = Seat_Log(seat_log_collection)
    payments = Payment_Log(payment_log_collection)

    seats.add_flight("EI179", 70, ["A", "B", "C", "D", "E", "F"])

    buyer = Person( "Joe", "Drumgoole", "21-May-2000")
    seat = seats.allocate_seat( "EI179", "1A", buyer )
    payments.make_payment( buyer, seat, 500, "USD")