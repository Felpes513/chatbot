# from datetime import datetime
# from services.bd import conectar
# from services import email_solicitacao
# from services.email_solicitacao import enviar_email_solicitacao

# # Função para cadastrar um novo pré-usuário
# def cadastrar_pre_usuario(nome, email_usuario):
#     try:
#         conn = conectar()
#         cursor = conn.cursor()

#         data_solicitacao = datetime.now()
#         status = 'pendente'

#         sql = "INSERT INTO pre_cadastro (nome, email, status, data_solicitacao) VALUES (%s, %s, %s, %s)"
#         valores = (nome, email_usuario, status, data_solicitacao)
#         cursor.execute(sql, valores)
#         conn.commit()

#         enviar_email_solicitacao(nome, email_usuario)

#         print(f"Cadastro solicitado com sucesso para {nome}. Aguardando aprovação do suporte.")

#     except Exception as e:
#         print(f"Erro ao cadastrar pré-usuário: {e}")

#     finally:
#         cursor.close()
#         conn.close()
