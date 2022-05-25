import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
CONN_STR = os.getenv('DB_URI')
DB_NAME = os.getenv('DB_NAME')

CLIENT = pymongo.MongoClient(CONN_STR, serverSelectionTimeoutMS=5000)
DB = CLIENT[DB_NAME]

async def test():
    return DB.get_collection('users')