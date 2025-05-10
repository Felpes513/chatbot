from datetime import datetime 
from app.services.bd import conectar
from app.services.email_solicitacao import enviar_email_solicitacao

def cadastrar_pre_usuario(nome, email, permissao, crm=None, estado_crm=None, caminho_assinatura=None):
    print(">>> Função cadastrar_pre_usuario() chamada")

    conn = None
    cursor = None
    try:
        conn = conectar()
        if not conn:
            print("Não foi possível conectar ao banco de dados.")
            return False, "Erro de conexão com o banco de dados."

        cursor = conn.cursor()

        data_solicitacao = datetime.now()
        status = 'pendente'

        # Inserção apenas dos campos que realmente existem na tabela
        sql = """
            INSERT INTO pre_cadastro (nome, email, permissao, data_solicitacao, status, crm, estado_crm)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nome, email, permissao, data_solicitacao, status, crm, estado_crm)
        cursor.execute(sql, valores)
        conn.commit()

        # Enviar e-mail com possível anexo da assinatura
        enviar_email_solicitacao(nome, email, permissao, crm, estado_crm, caminho_assinatura)

        print(f"Cadastro solicitado com sucesso para {nome}. Aguardando aprovação do suporte.")
        return True, "Cadastro solicitado com sucesso. Aguarde a aprovação."

    except Exception as e:
        print(f"Erro ao cadastrar pré-usuário: {e}")
        return False, f"Erro ao cadastrar: {e}"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()