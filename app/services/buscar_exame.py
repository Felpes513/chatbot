from app.services.bd import conectar

def buscar_exame_por_nome(nome_paciente):
    conn = conectar()
    cursor = conn.cursor()
    query = """
        SELECT exame_id, nome_paciente, data_exame, unidade, accession_number, status_exame
        FROM exames
        WHERE nome_paciente LIKE %s
    """
    try:
        cursor.execute(query, (f"%{nome_paciente}%",))
        resultados = cursor.fetchall()
    finally:
        conn.close()
    return resultados
