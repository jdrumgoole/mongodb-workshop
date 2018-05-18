
from datetime import datetime
from transactions.event_log import Event_Log
from transactions.flight import Person

class Payment(object):

    def __init__(self, person, item, amount, currency ):
        self._amount   = amount
        self._currency = currency
        self._item     = item
        self._person   = person

    def dict(self):
        return {"amount"   : self._amount,
                "currency" : self._currency,
                "item"     : self._item.dict(),
                "person"   : self._person.dict()}



class Payment_Log(Event_Log):

    def __init__(self, database, collection_name="payments_log"):
        super().__init__(database, collection_name)

    def initalise(self):
        super().initialise()
        self.make_payment( Person(), { "status:Initalised"},None, None)
        self._collection.create_index( {"ts":1})
        self._collection.create_index( {"person":1})
        self._collection.create_index( {"item":1})
        self._collection.create_index( {"person":1})


    def make_payment(self, person, item, amount, currency ):
        #
        # Contact payment processor here.
        #
        self.insert( { "amount"   : amount,
                       "currency" : currency,
                       "item"     : item.dict(),
                       "person"   : person.dict(),
                       "ts"       : datetime.utcnow()})

    def find_payment(self, amount=None, item=None, person=None ):

        query={}
        if amount:
            query["amount"] = amount
        if item:
            query[ "item"] = item
        if person:
            query["person"] = person

        return self._collection.find(query)

