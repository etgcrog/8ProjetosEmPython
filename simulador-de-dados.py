# Simulador de dado
# Simular o uso de um dado,gerando um valor de 1 até 6
from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout
        self.layout = [
            [sg.Text('Quer lançar o dado?',size=(15,0))],
            [sg.Button('SIM',size=(5,0)),sg.Button('NAO',size=(5,0))]
        ]

    def Iniciar(self):
        # Janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # Ler os Dados
        self.eventos, self.valores = self.janela.Read()
        # Fazer o iniciar

        if self.eventos == 'SIM' or self.eventos == 's':
            self.GerarValorDoDado()
            continuar = str(input("Quer continuar?[S/n]"))
        elif self.eventos == 'NAO' or self.eventos == 'n':
            print('Agrademos sua participação!')



    def GerarValorDoDado(self):
        computador = randint(self.valor_minimo, self.valor_maximo)
        print(computador)

simulador = SimuladorDeDado()
simulador.Iniciar()
