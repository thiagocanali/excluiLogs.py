import os
import time

# Defina o caminho onde os logs estão armazenados
caminho_logs = r"C:\caminho\para\seus\logs"  # Altere para o diretório real dos logs

# Defina o limite de tempo (7 dias em segundos)
limite_tempo = 7 * 24 * 60 * 60  # 7 dias em segundos

# Obtém o timestamp atual
tempo_atual = time.time()

# Itera sobre os arquivos no diretório de logs
for nome_arquivo in os.listdir(caminho_logs):
    caminho_arquivo = os.path.join(caminho_logs, nome_arquivo)

    # Verifica se o arquivo é um log (ajuste a condição conforme necessário)
    if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".log"):  # ajuste a extensão, se necessário
        # Obter a data de modificação do arquivo
        data_modificacao = os.path.getmtime(caminho_arquivo)

        # Verifica se o arquivo é mais antigo que 7 dias
        if tempo_atual - data_modificacao > limite_tempo:
            try:
                print(f"Excluindo o log: {nome_arquivo}")
                os.remove(caminho_arquivo)  # Remove o arquivo
            except Exception as e:
                print(f"Erro ao excluir {nome_arquivo}: {e}")
