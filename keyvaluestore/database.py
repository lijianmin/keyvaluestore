from pymongo import MongoClient

from keyvaluestore.settings import *

import urllib

class database:
    
    def getCollection(self, collection):
        
        client = MongoClient(MONGO_HOST, MONGO_PORT)

        db = client[MONGO_DATABASE]

        if MONGO_USER != "":
            db.authenticate(MONGO_USER, MONGO_USER_PASSWORD, mechanism='SCRAM-SHA-1')
        
        return db[collection]
