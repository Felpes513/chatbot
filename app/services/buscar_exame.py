import mysql.connector
from datetime import datetime
from app.services.bd import conectar

def buscar_exame_por_nome(nome, data_exame=None, cpf=None):
    conn = conectar()
<<<<<<< HEAD
    if not conn:
        return []

    try:
        cursor = conn.cursor(dictionary=True)

        
        cursor.execute("""
            SELECT * FROM exames WHERE nome_paciente = %s
        """, (nome_paciente,))
        resultados = cursor.fetchall()

        
        if not resultados:
            cursor.execute("""
                SELECT * FROM exames WHERE nome_paciente LIKE %s
            """, (f"%{nome_paciente}%",))
            resultados = cursor.fetchall()

        return resultados

    except Exception as e:
        print(f"Erro ao buscar exame: {e}")
        return []

    finally:
        cursor.close()
        conn.close()
=======
    cursor = conn.cursor(dictionary=True)

    try:
        # 1. Primeira tentativa: buscar apenas por nome
        query = "SELECT * FROM exames WHERE nome_paciente LIKE %s"
        cursor.execute(query, (f"%{nome}%",))
        resultados = cursor.fetchall()

        if resultados:
            return resultados, None  # Encontrou só com o nome

        # 2. Segunda tentativa: nome + data_exame
        if data_exame:
            query = """
                SELECT * FROM exames
                WHERE nome_paciente LIKE %s AND data_exame = %s
            """
            cursor.execute(query, (f"%{nome}%", data_exame))
            resultados = cursor.fetchall()
            if resultados:
                return resultados, None

        # 3. Terceira tentativa: nome + CPF
        if cpf:
            query = """
                SELECT * FROM exames
                WHERE nome_paciente LIKE %s AND cpf = %s
            """
            cursor.execute(query, (f"%{nome}%", cpf))
            resultados = cursor.fetchall()
            if resultados:
                return resultados, None

        # Nenhuma correspondência
        return [], "Nenhum exame encontrado com os dados fornecidos."

    finally:
        cursor.close()
        conn.close()
>>>>>>> e8c98a6 (Correção de falhas)
