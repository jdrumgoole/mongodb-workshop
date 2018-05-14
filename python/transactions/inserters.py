
import pymongo
from pymongo.write_concern import WriteConcern

class Timestamp(object);


    def __init__(collection, write_concern=None):

        self._collection =