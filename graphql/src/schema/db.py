from os import getenv
import pymongo

myclient = pymongo.MongoClient(getenv("MONGO_URL"))
db = myclient["mydatabase"]