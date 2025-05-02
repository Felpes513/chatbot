import schedule
import time
from app.services.limpar_cadastro import limpar_cadastros_pendentes

# Função para agendar a limpeza a cada 10 minutos
def agendar_limpeza():
    schedule.every(10).minutes.do(limpar_cadastros_pendentes)

    print("Agendador de limpeza iniciado...")

    while True:
        schedule.run_pending()
        time.sleep(1)
