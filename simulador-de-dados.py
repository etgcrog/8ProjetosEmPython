# Simulador de dado
# Simular o uso de um dado,gerando um valor de 1 até 6
from random import randint

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?[Sim/Não]:'

    def Iniciar(self):
        resp = input(self.mensagem) 
        try:
            if resp == 'sim' or resp == 's':
                self.GerarValorDoDado()
            elif resp == 'nao' or resp == 'n':
                print('Agrademos sua participação!')   
            else:
                while True:
                    if resp not in 'snsimnao':
                        print('Por favor, Digite sim ou não.')
                        break
        except:
            print('Ocorreu um erro ao receber sua resposta')



    def GerarValorDoDado(self):
        computador = randint(self.valor_minimo, self.valor_maximo)
        print(computador)

simulador = SimuladorDeDado()
simulador.Iniciar()

