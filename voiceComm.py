frase = []

# Palavras comuns para ignorar
ignore_words = ["por", "favor", "o", "a", "os", "as"]

def set_frase(f):
    global frase
    # Divide a frase e remove as palavras comuns
    frase = [word for word in f.lower().split() if word not in ignore_words]

# Função responsável por abrir o YouTube
def abrir_yt():
    print("Abrindo YouTube...")

# Função responsável por fechar o YouTube
def fechar_yt():
    print("Fechando YouTube...")

# Dicionário com comandos e funções associadas
subcommands = {
    "youtube": {
        "abrir": abrir_yt,
        "fechar": fechar_yt
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
