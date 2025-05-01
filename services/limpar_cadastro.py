# from datetime import datetime, timedelta
# from services.bd import conectar

# # Função para limpar cadastros pendentes depois de 1 hora
# def limpar_cadastros_pendentes():
#     try:
#         conn = conectar()
#         cursor = conn.cursor()

#         uma_hora_atras = datetime.now() - timedelta(hours=1)

#         sql = "DELETE FROM pre_cadastro WHERE status = 'pendente' AND data_solicitacao < %s"
#         valores = (uma_hora_atras,)
#         cursor.execute(sql, valores)
#         conn.commit()

#         print("Limpeza de pré-cadastros antigos concluída.")

#     except Exception as e:
#         print(f"Erro ao limpar pré-cadastros: {e}")

#     finally:
#         cursor.close()
#         conn.close()
