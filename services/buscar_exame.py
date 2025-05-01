from services.bd import conectar

# Função para buscar exames por nome do paciente
def buscar_exame_por_nome(nome_paciente):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT exame_id, nome_paciente, data_exame, unidade, accession_number, status_exame FROM exames WHERE nome_paciente LIKE %s"
    cursor.execute(query, ('%' + nome_paciente + '%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados