from app.core.mongodb.mongodb import mongodb_client
from app.core.mongodb.mongodb_path import DB1

class MongoCollection2:
    def __init__(self):
        self.db = mongodb_client().get_database(DB1.NAME)

    @property
    def c1(self):
        return self.db.get_collection(DB1.Collection.C1)

    @property
    def c2(self):
        return self.db.get_collection(DB1.Collection.C2)
