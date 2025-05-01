# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Configurações do e-mail
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_user = 'Chatbot'
# smtp_password = '961072115Felipe@'
# email_suporte = 'felipemoreira2003@gmail.com'  # Email do suporte

# # Função para enviar e-mail de solicitação de cadastro
# def enviar_email_solicitacao(nome, email_usuario):
#     mensagem = MIMEMultipart()
#     mensagem['From'] = smtp_user
#     mensagem['To'] = email_suporte
#     mensagem['Subject'] = 'Nova Solicitação de Cadastro - Chatbot MobileMed'

#     corpo = f"""
#     Olá, equipe de suporte!

#     Um novo pedido de cadastro foi realizado:

#     Nome: {nome}
#     E-mail: {email_usuario}

#     Vocês têm 1 hora para aprovar. Caso contrário, o cadastro será removido automaticamente.

#     Att,
#     Sistema MobileChat
#     """

#     mensagem.attach(MIMEText(corpo, 'plain'))

#     with smtplib.SMTP(smtp_server, smtp_port) as servidor:
#         servidor.starttls()
#         servidor.login(smtp_user, smtp_password)
#         servidor.send_message(mensagem)
