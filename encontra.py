import os
from utils import formata_tamanho

caminho_procura = input('Digite um caminho:')
termo = input('Qual termo você procura?')

contador = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo...', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho Formatado', formata_tamanho(tamanho))

            except PermissionError as e:
                print('Sem permisão.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido:', e)

print()
print(f'{contador} arquivo(s) encontado(s).')


