# Simulador de dado
# Simular o uso de um dado,gerando um valor de 1 até 6
from random import randint

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?[Sim/Não]:'

    def Iniciar(self):
        while True:
            resp = input(self.mensagem)
            if resp == 'sim' or resp == 's':
                self.GerarValorDoDado()
                continuar = str(input("Quer continuar?[S/n]"))
                if continuar == 's' or continuar == 'sim':
                    continue
                else:
                    print('Saindo do simulador...')
                    break
            elif resp == 'nao' or resp == 'n':
                print('Agrademos sua participação!')
                break



    def GerarValorDoDado(self):
        computador = randint(self.valor_minimo, self.valor_maximo)
        print(computador)

simulador = SimuladorDeDado()
simulador.Iniciar()

