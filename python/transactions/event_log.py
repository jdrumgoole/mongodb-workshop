class Event_Log(object):

    def __init__(self, database, collection_name="event_log"):
        self._database = database
        self._collection_name = collection_name
        self._collection = self._database[self._collection_name]

    def initalise(self):
        self.drop()
        self._collection = self._database[self._collection_name]

    def insert(self, doc):
        return self._collection.insert_one(doc)

    def insert(self, docs):
        return self._collection.insert_many(docs)

    def drop(self):
        return self._collection.drop()