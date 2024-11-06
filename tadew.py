import speech_recognition as sr


import voiceComm as vc
import functions as func

import time

# Função para ouvir o microfone e reconhecer a fala
def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        
        # Loop contínuo para manter o programa ativo até o comando de saída
        while True:
            print("Diga um comando: ")
            audio = microfone.listen(source)
            
            try:
                frase = microfone.recognize_google(audio, language='pt-BR')
                print("Você disse: " + frase)
                if(func.checar_frase(frase)): break

                # Atualiza a frase em voiceComm
                vc.set_frase(frase)
                
                # Recupera os comandos com base na frase atual
                commands = vc.getCommands()
                
                # Exibe a frase e os comandos para depuração
                print("Frase dividida:", vc.frase)
                print("Comandos gerados:", commands)
                
                # Executa diretamente a função associada ao comando encontrado
                if commands:
                    for funcao in commands.values():
                        funcao()  # Executa a função associada ao comando
                        break
                else:
                    print("Comando não reconhecido.")
                    
            except sr.UnknownValueError:
                print("Não entendi")
            
ouvir_microfone()

