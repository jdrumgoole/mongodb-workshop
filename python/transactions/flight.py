
from _datetime import datetime
from transactions.event_log import Event_Log

class Person(object):

    def __init__(self, first_name: str=None, last_name: str=None, DOB: str=None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB

    def dict(self):
        return {"first_name": self._first_name,
                "last_name": self._last_name,
                "DOB": self._DOB}

class Seat(object):

    def __init__(self, flight_no, seat_no):
        self._flight_no = flight_no
        self._seat_no   = seat_no
        self._ts        = datetime.utcnow()


    def dict(self):
        return { "flight_no" : self._flight_no,
                 "seat_no"   : self._seat_no,
                 "ts"        : self._ts}



class Allocated_Seat(Seat):

    def __init__(self, flight_no, seat_no, person ):
        super().__init__( flight_no, seat_no )
        self._person = person

    def dict(self):
        d = super().dict()
        d[ "person" ] = self._person.dict()
        return d


class Seat_Log(Event_Log):

    def __init__(self, collection_name="seat_log"):
        super().__init__(collection_name)

    def add_flight(self, flight_no: str, seat_rows: int, seat_letters: list) -> list:

        seats = []
        for i in range(1, seat_rows+1):
            for l in seat_letters :
                seats.append( Seat( flight_no, "{}{}".format(i,l)).dict())

        self.insert_many(seats)

        return seats

    def allocate_seat(self, flight_no: str, seat_no: object, person: Person) -> object:
        """

        :rtype: object
        """
        allocated_seat = Allocated_Seat( flight_no, seat_no, person)
        self.insert_one( allocated_seat.dict())
        return allocated_seat


    def deallocate_seat(self, flight_no, seat_no):
        seat = Seat( flight_no, seat_no)
        self._collection.insert_one(seat.dict())
        return seat