import pymongo
from pymongo import IndexModel, ASCENDING
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
    


# Crear índice en el campo 'equipo'
collection.create_indexes([
    IndexModel([("equipo", ASCENDING)])
])

# Crear índice en el campo 'pais'
collection.create_indexes([
    IndexModel([("pais", ASCENDING)])
])

# Crear índice en el campo 'start_year'
collection.create_indexes([
    IndexModel([("start_year", ASCENDING)])
])

print("Índices creados exitosamente.")
