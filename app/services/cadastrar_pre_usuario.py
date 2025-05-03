from datetime import datetime 
from app.services.bd import conectar
from app.services.email_solicitacao import enviar_email_solicitacao

def cadastrar_pre_usuario(nome, email_usuario):
    print(">>> Função cadastrar_pre_usuario() chamada")

    conn = None
    cursor = None
    try:
        conn = conectar()
        if not conn:
            print("Não foi possível conectar ao banco de dados.")
            return

        cursor = conn.cursor()

        data_solicitacao = datetime.now()
        status = 'pendente'

        sql = """
            INSERT INTO pre_cadastro (nome, email, status, data_solicitacao)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nome, email_usuario, status, data_solicitacao)
        cursor.execute(sql, valores)
        conn.commit()

        enviar_email_solicitacao(nome, email_usuario)

        print(f"Cadastro solicitado com sucesso para {nome}. Aguardando aprovação do suporte.")

    except Exception as e:
        print(f"Erro ao cadastrar pré-usuário: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
