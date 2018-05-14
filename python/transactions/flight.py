

class Seat(object):

    def __init__(self, flight_no, seat_no):

        self._seat = { "flight": flight_no, "seat" : seat_no}

    def dict(self):
        return self._seat

class Flight(object):

    def __init__(self, database):
        self._seat_collection = database["seats"]
        self._seats = []
        self._seat_collection.insert( { "dummy": "nonce"}) #force collection into existence

    def collection(self):
        return self._seat_collection

    @staticmethod
    def make_flight( flight_no, seat_rows, seat_letters):

        seats = []
        for i in range(1, seat_rows+1):
            for l in seat_letters :
                seats.append( Seat( flight_no, "{}{}".format(i,l)).dict())

        return seats

    def no_txn_insert(self, seats):
        return self._seat_collection.insert_many(self._seats)

    def no_txn_make_flight(self, flight_no, seat_rows, seat_letters):

        self._seats = Flight.make_flight( flight_no, seat_rows, seat_letters)
        return self.no_txn_insert(self._seats)
