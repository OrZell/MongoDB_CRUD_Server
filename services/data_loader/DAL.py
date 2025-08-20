from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from services.soldier import Soldier

class DAL:

    def __init__(self):
        self.host = 'localhost'
        self.port = 27017
        self.db = 'enemy_soldiers'
        self.collection = 'soldier_details'
        self.connection = None

    def create_index(self):
        col = self.connection[self.db][self.collection]
        col.create_index([("ID", ASCENDING)])

    def open_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.host, self.port)

    def get_data(self):
        connection = self.connection
        return connection[self.db][self.collection].find({}, {"_id":0}).to_list(None)

    def post_data(self, ID, first_name, last_name, phone_number, rank):
        connection = self.connection
        soldier = Soldier(ID=ID, first_name=first_name, last_name=last_name, phone_number=phone_number, rank=rank)
        connection[self.db][self.collection].insert_one(soldier)
        return 'posted'

    def put_data_by_id(self, ID):
        connection = self.connection
        soldier = connection[self.db][self.collection].find_one({}, {"ID":ID, "_id":0})
        if soldier:
            return soldier

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = None