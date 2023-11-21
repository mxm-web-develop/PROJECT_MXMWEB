from motor.motor_asyncio import AsyncIOMotorClient
class MongoDB:
    client: AsyncIOMotorClient = None

mongo_db = MongoDB()

async def connect_to_mongo():
    username = "root"
    password = "12345"
    db_name = "mxmdb"
    mongo_db.client = AsyncIOMotorClient(f"mongodb://{username}:{password}@localhost:27017/{db_name}")

async def close_mongo_connection():
    mongo_db.client.close()
