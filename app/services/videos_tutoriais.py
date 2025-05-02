from app.services.bd import conectar

# Retorna vídeos tutoriais conforme o e-mail do usuário
def buscar_videos_por_email(email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT permissao FROM usuarios WHERE email = %s", (email,))
    resultado = cursor.fetchone()

    if not resultado:
        return None, "E-mail não encontrado. Por favor, verifique e tente novamente."

    tipo_usuario = resultado[0]

    cursor.execute("""
        SELECT titulo, url 
        FROM videos_tutoriais 
        WHERE permissao = %s AND ativo = TRUE
    """, (tipo_usuario,))
    videos = cursor.fetchall()
    conn.close()

    if not videos:
        return [], "Nenhum vídeo disponível para o seu perfil no momento."

    return videos, None
