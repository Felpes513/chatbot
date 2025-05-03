from dotenv import load_dotenv
load_dotenv()

import mysql.connector
from config.db_config import db_config
print("Configuração de banco carregada:", db_config)

def conectar():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso.")
            return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return None
