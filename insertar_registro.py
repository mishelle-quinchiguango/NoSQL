import pymongo

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



# Datos a insertar
jugadora = {
    "_id": 12345,
    "nombre": "Estefania",
    "apellido": "Quinchiguango",
    "edad": 25,
    "ocupacion": "Futbolista",
    "equipo": "Manchester United",
    "start_year": 2021,
    "pais": "España",
    "posicion": "Delantera",
    "estadisticas": {
        "goles": 30,
        "pases": 45
    },
    "condicion_fisica": {
        "peso": 58.5,
        "altura": 1.67,
        "enfermedades": ["Asma"],
        "categoria": "Profesional",
        "grupo_sanguineo": "A+"
    }
}


collection.insert_one(jugadora)

print("Datos insertados correctamente en MongoDB.")
