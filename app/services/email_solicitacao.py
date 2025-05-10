import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

# Configurações do e-mail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'felipemoreira2003@gmail.com'
smtp_password = os.getenv('SMTP_PASSWORD')  # Defina essa variável no ambiente
email_suporte = 'felipe.moreira@uscsonline.com.br'

def enviar_email_solicitacao(nome, email, permissao=None, crm=None, estado_crm=None, caminho_assinatura=None):
    mensagem = MIMEMultipart()
    mensagem['From'] = smtp_user
    mensagem['To'] = email_suporte
    mensagem['Subject'] = 'Nova Solicitação de Cadastro - Chatbot MobileMed'

    corpo = f"""\
Olá, equipe de suporte!

Um novo pedido de cadastro foi realizado:

Nome: {nome}
E-mail: {email}
Permissão Solicitada: {permissao or 'Não informada'}"""

    if permissao == "Médico":
        corpo += f"""
CRM: {crm or 'Não informado'}
Estado do CRM: {estado_crm or 'Não informado'}
Assinatura enviada: {'Sim' if caminho_assinatura else 'Não'}"""

    corpo += """

Vocês têm 1 hora para aprovar. Caso contrário, o cadastro será removido automaticamente.

Att,
Sistema MobileChat
"""

    mensagem.attach(MIMEText(corpo, 'plain', 'utf-8'))

    # Anexar assinatura, se existir
    if caminho_assinatura and os.path.exists(caminho_assinatura):
        with open(caminho_assinatura, 'rb') as f:
            file_data = f.read()
            filename = os.path.basename(caminho_assinatura)

            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                part = MIMEImage(file_data)
            else:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file_data)
                encoders.encode_base64(part)

            part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            mensagem.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as servidor:
            servidor.starttls()
            servidor.login(smtp_user, smtp_password)
            servidor.send_message(mensagem)
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")