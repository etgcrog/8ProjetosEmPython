import os

path = '/home/edudev/Downloads'

files = os.listdir(path)

def pegar_extensao(nomes):
    index = nomes.rfind('.')
    print(nomes[index:])

if __name__ == '__main__':
    for file in files:
        pegar_extensao(file)