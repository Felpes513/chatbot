from datetime import datetime, timedelta
from app.services.bd import conectar

# Função para limpar cadastros pendentes depois de 1 hora
def limpar_cadastros_pendentes():
    conn = None
    cursor = None
    try:
        conn = conectar()
        if not conn:
            print("Erro: conexão com banco de dados não estabelecida.")
            return

        cursor = conn.cursor()
        uma_hora_atras = datetime.now() - timedelta(hours=1)

        sql = """
            DELETE FROM pre_cadastro 
            WHERE status = 'pendente' AND data_solicitacao < %s
        """
        cursor.execute(sql, (uma_hora_atras,))
        conn.commit()

        print("Limpeza de pré-cadastros antigos concluída.")

    except Exception as e:
        print(f"Erro ao limpar pré-cadastros: {e}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()