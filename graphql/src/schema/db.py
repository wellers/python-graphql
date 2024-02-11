from os import getenv
import motor.motor_asyncio as motor

def connect():
	myclient = motor.AsyncIOMotorClient(getenv("MONGO_URL"))
	return myclient["mydatabase"]