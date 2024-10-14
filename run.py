from models.connection_options.connection import DBConnectionHandler
from models.repository.Usuarios_repository import UsuariosRepository
from app.module import main
"""
db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

usuarios = UsuariosRepository(db_connection)

order = {
    "name": "Pedro",
    "endereco": "Rua dois",
    "pedidos": {
        "pizza": "1",
        "refrigerante": "1"
    }
}

usuarios.insert_document(order)"""

main()