from libsql_client.dbapi2 import connect

url = "sqlite+libsql://petsalud-tomvalen.turso.io"
# Configurar el token de autenticación
auth_token = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MzU3Nzc5NTksImlkIjoiMzNiMDQ0NWQtZDZiZS00ZTViLTk0NGMtZjBkNGE4OWE0ZDM3In0._3A71MLFPxm5Msuilk-TzimNHzDSz8UgNZbhJ1LqDaeMauvGFEJQi3Dn4aNRys6ugidnAoM19nN7HbtPQy8LAw"

try:
    # Establecer conexión
    conn = connect(url, auth=auth_token)
    print("Conexión exitosa")
except Exception as e:
    print(f"Error al conectar: {e}")