# from services.bd import conectar

# # Função para exibir vídeos tutoriais conforme o perfil do usuário
# def exibir_videos_tutoriais(email):
#     conn = conectar()
#     cursor = conn.cursor()

#     cursor.execute("SELECT permissao FROM usuarios WHERE email = %s", (email,))
#     resultado = cursor.fetchone()

#     if not resultado:
#         print("E-mail não encontrado. Por favor, verifique e tente novamente.")
#         return

#     tipo_usuario = resultado[0]

#     cursor.execute("""
#         SELECT titulo, url 
#         FROM videos_tutoriais 
#         WHERE permissao = %s AND ativo = TRUE
#     """, (tipo_usuario,))
#     videos = cursor.fetchall()
#     conn.close()

#     if not videos:
#         print("Nenhum vídeo disponível para o seu perfil no momento.")
#         return

#     print("\nVídeos disponíveis:")
#     for titulo, url in videos:
#         print(f"- {titulo}: {url}")
