import pandas as pd
import random

# Listas de datos aleatorios
nombres = ["Mishelle", "Laura", "Sofía", "Elena", "Lizhet", "María", "Carmen", "Melissa", "Raquel", "Patricia", 
           "Liliana", "Cristina", "Dayana", "Paula", "Natalia", "Blanca", "Adriana", "Verónica", "Isabel", "Gabriela"]
apellidos = ["González", "Martínez", "Jiménez", "Suárez", "Fernández", "Ruiz", "Díaz", "López", "García", 
             "Moreno", "Navarro", "Serrano", "Gómez", "Sanz", "Cruz", "Ramírez", "Vega", "Pérez", "Ortega"]
equipos = ["Real Madrid", "Barcelona", "Juventus", "Arsenal", "Olympique Lyon", "Inter de Milán", "Chelsea", 
           "Manchester United", "Valencia", "Sevilla", "Liverpool", "Manchester City", "Borussia Dortmund"]
paises = ["España", "Italia", "Alemania", "Portugal", "Suecia", "Austria", "Dinamarca", "Polonia"]
posiciones = ["Delantera", "Mediocampista", "Defensora", "Portera"]
categorias = ["A", "B", "C"]
grupos_sanguineos = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
enfermedades = ["Ninguna", "Asma", "Tendinitis", "Lesión de rodilla"]

# Función para generar cédulas únicas
def generar_cedula():
    return f"{random.randint(1000000000, 9999999999)}"

# Generar datos
data = []
cedulas_generadas = set()
for i in range(100):
    cedula = generar_cedula()
    while cedula in cedulas_generadas:
        cedula = generar_cedula()  # Asegurar cédulas únicas
    cedulas_generadas.add(cedula)
    
    registro = {
        "_id": cedula,
        "nombre": random.choice(nombres),
        "apellido": random.choice(apellidos),
        "edad": random.randint(18, 40),
        "equipo": random.choice(equipos),
        "start_year": random.randint(2015, 2023),
        "pais": random.choice(paises),
        "posicion": random.choice(posiciones),
        "goles": random.randint(0, 50),
        "pases": random.randint(50, 200),
        "peso": round(random.uniform(50.0, 80.0), 1),
        "altura": round(random.uniform(1.50, 1.90), 2),
        "enfermedades": random.choice(enfermedades),
        "categoria": random.choice(categorias),
        "grupo_sanguineo": random.choice(grupos_sanguineos),
    }
    data.append(registro)


# Crear DataFrame y guardar en CSV
df = pd.DataFrame(data)
output_path = "data_jugadoras.csv"
df.to_csv(output_path, index=False, encoding="utf-8")
print(f"Archivo CSV fue creado en: {output_path}")
