from os import getenv
import motor.motor_asyncio as motor

def connect():
	mongo_url = getenv("MONGO_URL")
	mongo_database = getenv("MONGO_DATABASE")
	myclient = motor.AsyncIOMotorClient(mongo_url)
	return myclient[mongo_database]