import functions as func

frase = []

# Palavras comuns para ignorar
ignore_words = ["por", "favor", "o", "a","é", "os", "as", "que", "tadeu"]

def set_frase(f):
    global frase
    # Divide a frase e remove as palavras comuns
    frase = [word for word in f.lower().split() if word not in ignore_words]

# Dicionário com comandos e funções associadas
subcommands = {
    "youtube": {
        "abrir": func.abrir_yt,
        "fechar": func.fechar_yt
    },
    "google": {
        "abrir": func.abrir_google,
        "fechar": func.fechar_google
    },
    "são": {
        "horas": func.hora_atual
    },
    "hoje": {
        "dia": func.data_atual
    }
}

# Função que retorna os comandos, configurados dinamicamente com base na frase
def getCommands():
    if len(frase) >= 2:
        action = frase[0]  # Exemplo: "abrir" ou "fechar"
        target = frase[1]  # Exemplo: "youtube"
        
        # Verifica se o target e action existem no dicionário subcommands
        if target in subcommands:
            if action in subcommands[target]:
                print(f"Comando encontrado: {action} {target}")  # Depuração
                return {action: subcommands[target][action]}
            else:
                print(f"Ação '{action}' não encontrada para '{target}'")  # Depuração
        else:
            print(f"Target '{target}' não encontrado")  # Depuração
    
    # Retorna um dicionário vazio se não encontrar o comando
    return {}
