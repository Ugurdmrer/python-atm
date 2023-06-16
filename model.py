from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')


db = client.atm

collection = db.clients


def getAllUsers():
    cursor = collection.find({})
    data = []
    if len(data) == 0:
        print("veri yok ")
    else:
        for client in cursor:

            data.append(client)
            return data