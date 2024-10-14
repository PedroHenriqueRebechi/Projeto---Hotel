from typing import Dict

class UsuariosRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "Usuarios"
        self.__db_conection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_conection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document