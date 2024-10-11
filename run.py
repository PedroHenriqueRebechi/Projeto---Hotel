from models.connection_options.connection import DBConnectionHandler

db_handle = DBConnectionHandler()
conn1 = db_handle.get_db_connection()
print(conn1)

db_handle.connect_to_db()
conn2 = db_handle.get_db_connection()
print(conn2)