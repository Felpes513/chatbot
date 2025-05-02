import mysql.connector
from config.db_config import db_config  # Importando as configurações de banco de dados

def conectar():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso.")
            return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return None  # Garantir que retorna None se não conectar
