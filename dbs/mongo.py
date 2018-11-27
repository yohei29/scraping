from pymongo import MongoClient

client = MongoClient('localhost', )

db = client['test']

clectin = db.sports
clectin.insert_one({'name':'apple'})

for v in clectin.find():
    print(v)