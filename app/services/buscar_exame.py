from app.services.bd import conectar

def buscar_exame_por_nome(nome_paciente):
    conn = conectar()
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