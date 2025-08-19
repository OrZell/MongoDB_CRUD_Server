from pymongo import MongoClient

class DAL:

    def __init__(self):
        self.host = 'localhost'
        self.port = 27017
        self.db = 'enemy_soldiers'
        self.collection = 'soldier_details'
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.host, self.port)
        return self.connection


    def get(self):
        connection = self.get_connection()
        return connection[self.db][self.collection].find()

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = None