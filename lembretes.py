import pyautogui
import time
from datetime import datetime, timedelta

# Mensagem inicial
pyautogui.alert("Bom dia! Não se esqueça de se manter-se hidratada(o) e de fazer pequenas pausas ao longo do dia para comer algo leve! Tenha um ótimo dia!")

# Intervalos em segundos
intervalo_agua = 3600  # 1 hora
intervalo_comida = 10800  # 3 horas
pausa_almoço = 3600  # 1 hora para o almoço
duracao_total = 32400  # 9 horas em segundos

# Tempo total de execução
tempo_passado = 0

# Horário do início
horario_inicio = datetime.now()

while tempo_passado < duracao_total:
    # Lembrete para tomar água
    pyautogui.alert("Hora de tomar água! Hidrate-se!")
    time.sleep(intervalo_agua)
    tempo_passado += intervalo_agua
    
    # Verifica se é hora de comer a cada 3 horas
    if tempo_passado % intervalo_comida == 0:
        # Verifica se já passou o horário do almoço
        if datetime.now() < horario_inicio + timedelta(hours=5):  # Almoço até 5 horas após o início
            pyautogui.alert("Hora de comer! Não esqueça de se alimentar!")
        else:
            pyautogui.alert("Hora do almoço! Faça uma pausa de 1 hora.")
            time.sleep(pausa_almoço)  # Pausa para o almoço
            tempo_passado += pausa_almoço  # Adiciona a pausa ao tempo passado

    # Verifica se o tempo total foi atingido
    if datetime.now() >= horario_inicio + timedelta(hours=9):
        pyautogui.alert("Fim de expediente! Tenha um bom retorno, boa noite e bom descanso!.")
        break