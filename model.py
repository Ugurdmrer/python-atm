# Database bağlantısı
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.atm

collection = db.clients
