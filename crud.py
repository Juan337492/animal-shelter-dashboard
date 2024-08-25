from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]
    # Method to implement C in CRUD
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True 
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")
     #Method to implement R in CRUD
    def read(self, search_data):
        try:
            if search_data:
                data = self.collection.find(search_data, {"_id": False})
            else:
                data = self.collection.find({}, {"_id": False})
            return list(data)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    #Method to implement U in CRUD
    def update(self, search_data, update_data):
        if search_data is not None and update_data is not None:
            try:
                result = self.collection.update_many(search_data, {"$set": update_data})
                return result.raw_result
            except Exception as e:
                print(f"An error occurred: {e}")
                return{}
        else:
            raise ValueError("Search data or update parameter is empty")
    #Method to implement D in CRUD
    def delete(self, delete_data):
        if delete_data is not None:
            try:
                result = self.collection.delete_many(delete_data)
                return result.raw_result
            except Exception as e:
                print(f"An error occurred: {e}")
                return {}
        else:
            raise ValueError("Delete data parameter is empty")
            
