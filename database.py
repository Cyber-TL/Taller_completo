from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

MONGODB_URL = config("MONGODB_URL", default="mongodb://localhost:27017")
DATABASE_NAME = config("DATABASE_NAME", default="adso_db")

client = AsyncIOMotorClient(MONGODB_URL)

database = client[DATABASE_NAME]

coleccion_tareas = database["tareas"]

async def verificar_conexion():
    try:
        await client.admin.command("ping")
        print(f"Conexión exitosa a la base de datos: '{DATABASE_NAME}'")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")