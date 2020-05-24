from random import randint
from time import sleep
class JogoAdvinhar:
    def __init__(self):
        self.acertou = False

    def Iniciar(self):
        sleep(1)
        print('Acabei de pensar em número de 1 até 10. Tente acertar!!!')
        self.ValorDoComputador()
        tentativas = 0
        while not self.acertou:
            self.ValorDoJogador()
            tentativas += 1
            if self.computador == self.jogador:
                print('Você ACERTOU, PARABÉNS')
                self.acertou = True
            else:
                if self.jogador < self.computador:
                    print('Tente um número maior...')
                elif self.jogador > self.computador:
                    print('Tente um número menor...')
        print(f'Acertou com {tentativas}. Parabéns e volte sempre!')
        
    def ValorDoJogador(self):
        self.jogador = int(input('Qual é o seu palpite? '))

    def ValorDoComputador(self):
        self.computador = randint(1,100)

jogar = JogoAdvinhar()
jogar.Iniciar()