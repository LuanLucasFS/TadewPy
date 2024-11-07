import ollama
import text_to_speech

def set_frase(f):
    global frase 
    frase = f

def fazer_pergunta():
    text_to_speech.cria_audio("Um momento enquanto faço a pesquisa")

    try:
        # Iniciar o stream de mensagens com a pergunta
        stream = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': frase.replace("fazer perguntas", "")}],  # Pergunta enviada como dicionário
            stream=True,
        )

        # Usar uma lista para acumular partes da resposta
        resposta_chunks = []

        for chunk in stream:
            # Verifique se 'chunk' e 'chunk['message']' são dicionários
            if isinstance(chunk, dict) and 'message' in chunk:
                message = chunk['message']
                # Certifique-se de que 'message' é um dicionário e que contém 'content'
                if isinstance(message, dict) and 'content' in message:
                    resposta_chunks.append(message['content'])
                else:
                    print(f"Erro: 'content' não encontrado em 'message'.")
            else:
                print(f"Erro: 'chunk' não é um dicionário ou não contém 'message'.")

        # Juntar as partes da resposta em uma única string
        resposta_completa = "".join(resposta_chunks).strip()  # Remover espaços extras no final

        # Verificar se a resposta é válida antes de criar o áudio
        if resposta_completa:
            print("Resposta do modelo:", resposta_completa)  # Opcional, para verificar o conteúdo
            text_to_speech.cria_audio(resposta_completa.replace("*", ""))  # Gerar áudio se houver conteúdo
        else:
            print("A resposta está vazia. Nenhum áudio será gerado.")

    except ollama._types.ResponseError as e:
        print(f"Erro ao fazer a pergunta: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
