from pymongo import MongoClient

connection_string = "mongodb+srv://pedrohenriquerebechi:fUXsBfttSzS2y2PJ@cluster0.m7udj.mongodb.net/"
client = MongoClient(connection_string)
db_connection = client["HotelProject"] # Conecta com Projeto

usuarios_collection = db_connection.get_collection("Usuarios") # Conecta com Database

search_filter = {"ola": "mundo"} # Filtro de busca no banco

response = usuarios_collection.find(search_filter) 

for registry in response: print(registry)