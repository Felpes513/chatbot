import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do e-mail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'felipemoreira2003@gmail.com'
smtp_password = 'gnmq rotb stmw tvvx'    # <-- Gerada em https://myaccount.google.com/apppasswords
email_suporte = 'felipe.moreira@uscsonline.com.br'

def enviar_email_solicitacao(nome, email_usuario, permissao=None, crm=None, estado_crm=None, caminho_assinatura=None):
    mensagem = MIMEMultipart()
    mensagem['From'] = smtp_user
    mensagem['To'] = email_suporte
    mensagem['Subject'] = 'Nova Solicitação de Cadastro - Chatbot MobileMed'

    # Corpo do e-mail
    corpo = f"""
    Olá, equipe de suporte!

    Um novo pedido de cadastro foi realizado:

    Nome: {nome}
    E-mail: {email_usuario}
    Permissão Solicitada: {permissao or 'Não informada'}
    """

    # Se o usuário for médico, inclua CRM, estado do CRM e assinatura
    if permissao == "Médico":
        corpo += f"""
        CRM: {crm or 'Não informado'}
        Estado do CRM: {estado_crm or 'Não informado'}
        Assinatura enviada: {'Sim' if caminho_assinatura else 'Não'}
        """

    corpo += """
    Vocês têm 1 hora para aprovar. Caso contrário, o cadastro será removido automaticamente.

    Att,
    Sistema MobileChat
    """

    mensagem.attach(MIMEText(corpo, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as servidor:
            servidor.starttls()
            servidor.login(smtp_user, smtp_password)
            servidor.send_message(mensagem)
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
