import time


import text_to_speech as tts
import converter_data as cd


# Função para checar se o programa deve ser finaizado
def checar_frase(frase):
    # Condição para encerrar o loop
    if frase.lower() in ["fechar tadew", "fechar tadeu"]:
        print("Encerrando o programa...")
        return True

# Função para abrir o YouTube
def abrir_yt():
    tts.cria_audio("Abrindo YouTube...")

# Função para fechar o YouTube
def fechar_yt():
    tts.cria_audio("Fechando YouTube...")

# Função para abrir o Google Chrome
def abrir_google():
    tts.cria_audio("Abrindo Google")

# Função para fechar o Google Chrome
def fechar_google():
    tts.cria_audio("Fechando Google")


def hora_atual():
    hora = f"{time.localtime().tm_hour}:{time.localtime().tm_min}"
    tts.cria_audio("Agora são: " + hora)


def data_atual():
    data = cd.converter_data()
    tts.cria_audio(f"Hoje é: {data}")