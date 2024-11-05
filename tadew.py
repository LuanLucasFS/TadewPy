import speech_recognition as sr
import voiceComm

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
                
                # Condição para encerrar o loop
                if frase.lower() in ["fechar tadew", "fechar tadeu"]:
                    print("Encerrando o programa...")
                    break
                
                # Atualiza a frase em voiceComm
                voiceComm.set_frase(frase)
                
                # Recupera os comandos com base na frase atual
                commands = voiceComm.getCommands()
                
                # Exibe a frase e os comandos para depuração
                print("Frase dividida:", voiceComm.frase)
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

# Inicia o loop de escuta
ouvir_microfone()
