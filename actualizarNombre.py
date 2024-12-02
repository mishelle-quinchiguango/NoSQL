import pymongo
from datetime import datetime, timedelta
import pandas as pd

# URL de conexión
mongo_url = "mongodb+srv://mishellequinchiguango:Sistemas9.@cluster0.obql6.mongodb.net/"

# Conexión a MongoDB
try:
    client = pymongo.MongoClient(mongo_url)
    db = client["JugadorasFemeninas"]  # Base de datos 'JugadorasFemeninas'
    collection = db["jugadoras"]  # Colección 'jugadoras'
    print("Conexión exitosa a MongoDB Atlas")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}") 
    

jugadora = collection.find_one({"_id": 9408936022})

if jugadora:
    nuevo_nombre = jugadora["nombre"].upper()

    collection.update_one(
        {"_id": 5658520424},
        {"$set": {"nombre": nuevo_nombre}}
    )
    print("Nombre actualizado a mayúsculas:", nuevo_nombre)
else:
    print("No se encontró la jugadora con el ID especificado.")
