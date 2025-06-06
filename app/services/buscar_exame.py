import mysql.connector
from datetime import datetime
from app.services.bd import conectar

def buscar_exame_por_nome(nome, data_exame=None, cpf=None):
    conn = conectar()
    if not conn:
        return [], "Erro na conexão com o banco de dados."

    cursor = conn.cursor(dictionary=True)

    try:
        # 1. Primeira tentativa: buscar apenas por nome
        query = "SELECT * FROM exames WHERE nome_paciente LIKE %s"
        cursor.execute(query, (f"%{nome}%",))
        resultados = cursor.fetchall()

        if resultados:
            return resultados, None  # Encontrou só com o nome

        # 2. Segunda tentativa: buscar apenas por data_exame (se fornecida)
        if data_exame:
            query = """
                SELECT * FROM exames
                WHERE data_exame = %s
            """
            cursor.execute(query, (data_exame,))
            resultados = cursor.fetchall()
            if resultados:
                return resultados, None  # Encontrou pela data

        # 3. Terceira tentativa: buscar apenas por CPF (se fornecido)
        if cpf:
            query = """
                SELECT * FROM exames
                WHERE cpf = %s
            """
            cursor.execute(query, (cpf,))
            resultados = cursor.fetchall()
            if resultados:
                return resultados, None  # Encontrou pelo CPF

        # Nenhuma correspondência
        return [], "Nenhum exame encontrado com os dados fornecidos."

    except Exception as e:
        print(f"Erro ao buscar exame: {e}")
        return [], "Erro interno ao buscar exame."

    finally:
        cursor.close()
        conn.close()