from gtts import gTTS
from playsound import playsound
import time
import os
import uuid

# Função responsável por criar o áudio
def cria_audio(audio):
    # Verifica e cria o diretório 'audios' se ele não existir
    os.makedirs('audios', exist_ok=True)
    
    # Gera um nome de arquivo único
    file_path = f'audios/{uuid.uuid4()}.mp3'
    
    # Cria o áudio
    tts = gTTS(audio, lang='pt-br')
    
    # Salva o arquivo de áudio
    tts.save(file_path)
    print("Estou aprendendo o que você disse...")
    
    # Reproduz o áudio
    playsound(file_path)
    time.sleep(1)
    
    # Remove o arquivo depois de tocar
    os.remove(file_path)