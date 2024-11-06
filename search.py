import voiceComm as vc

frase = "que horas são"

vc.set_frase(frase)
commands = vc.getCommands()


if commands:
    for funcao in commands.values():
        funcao()  # Executa a função associada ao comando
        break
else:
    print("Comando não reconhecido.")