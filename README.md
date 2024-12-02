# NoSQL
Dependencias: Se pueden instalar las dependencias ejecutando: 
pip install -r requirements.txt
##Configuración de la Base de Datos
Conexión a MongoDB: Se puede modificar la cadena de conexión en el script para conectar a un servidor remoto si es necesario.
##Ejecución de los Scripts
1. Inserción de Datos desde CSV:
Ejecuta el script para insertar registros:
python generarData.py
Ete script lee los datos desde el archivo CSV y los inserta en la colección jugadoras de MongoDB.
2. Consultas y Modificaciones:
Las consultas y modificaciones se encuentran en el archivo SentenciasUtilizadas.
3. Optimización con Índices
Para mejorar el rendimiento de las consultas, se agregaron índices en los siguientes campos:

    equipo: Búsquedas por equipo.
    pais: Filtrado por país.
    start_year: Filtrado por año de inicio.

Para verificar los tiempos de ejecución, utiliza explain("executionStats") en MongoDB por ejemplo:
db.jugadoras.find({
  "equipo.nombre": { $regex: /^Manchester/, $options: "i" }
}).explain("executionStats")
