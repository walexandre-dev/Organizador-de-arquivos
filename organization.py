#importações das bibliotecas que usaremos neste projeto:
import os
import shutil
import time
from datetime import datetime

PASTA_ALVO = "C:\\Users\\Adimi\\Downloads"

REGRAS_POR_EXTENSAO = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".odt", ".rtf"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Músicas": [".mp3", ".wav", ".aac", ".flac"],
    "Arquivos Compactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "Executáveis e Instaladores": [".exe", ".msi", ".dmg"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Outros": [] # Pasta para tudo que não se encaixar nas outras regras
}

def encontrar_pasta_destino(extensao):
    """Encontra o nome da pasta de destino com base na extensão do arquivo."""
    for nome_pasta, extensoes in REGRAS_POR_EXTENSAO.items():
        if extensao in extensoes:
            return nome_pasta
    return "Outros" # Retorna a pasta padrão se nenhuma regra corresponder

def organizar_por_extensao(pasta_alvo):
    print(f"Iniciando organização da pasta: {pasta_alvo}\n")
    arquivos_movidos = 0
    
    try:
        # Lista todos os itens (arquivos e pastas) no diretório alvo
        for nome_arquivo in os.listdir(pasta_alvo):
            caminho_arquivo_origem = os.path.join(pasta_alvo, nome_arquivo)

            # Verifica se é um arquivo e não uma pasta
            if os.path.isfile(caminho_arquivo_origem):
                # Extrai a extensão do arquivo e a converte para minúsculas
                _, extensao = os.path.splitext(nome_arquivo)
                extensao = extensao.lower()

                # Encontra a pasta de destino com base na regra
                nome_pasta_destino = encontrar_pasta_destino(extensao)
                caminho_pasta_destino = os.path.join(pasta_alvo, nome_pasta_destino)

                # Cria a pasta de destino se ela não existir
                if not os.path.exists(caminho_pasta_destino):
                    print(f"Criando pasta: {caminho_pasta_destino}")
                    os.makedirs(caminho_pasta_destino)
                
                # Monta o caminho final para o arquivo
                caminho_arquivo_destino = os.path.join(caminho_pasta_destino, nome_arquivo)

                # Move o arquivo para a pasta de destino
                try:
                    print(f"Movendo '{nome_arquivo}' para '{nome_pasta_destino}'...")
                    shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
                    arquivos_movidos += 1
                except Exception as e:
                    print(f"ERRO ao mover '{nome_arquivo}': {e}")

    except FileNotFoundError:
        print(f"ERRO: A pasta '{pasta_alvo}' não foi encontrada. Verifique o caminho.")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return

    print(f"\nOrganização concluída!")
    print(f"Total de arquivos movidos: {arquivos_movidos}")


# --- PONTO DE ENTRADA DO SCRIPT ---
if __name__ == "__main__":
        organizar_por_extensao(PASTA_ALVO)
