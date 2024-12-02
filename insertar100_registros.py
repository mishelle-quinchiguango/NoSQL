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
# Leer el CSV
# Obtener todos los documentos
registros = collection.find()

# Mostrar los documentos
for registro in registros:
    print(registro)