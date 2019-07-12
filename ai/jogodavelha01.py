# jogo da velha
# coding: utf-8
class Jogador:
    def __init__(self, simbolo):
        self.simbolo = simbolo
    

class Tabuleiro:
    def __init__(self):
        # nove casas, iniciando da primeira casa à esquerda e acima do tabuleiro
        self.casas = [" "," "," "," "," "," "," "," "," "]
        #
        # [0] [1] [2]
        # [3] [4] [5]
        # [6] [7] [8]
        # 

    def escrever(self, casa):
        row = " ___ ___ ___ \n"
        for i in range(0,9):
            row += "| " + self.casas[i] + " "
            if (((i+1) % 3) == 0):
                row += "|\n"
                row +=  "|___|___|___|\n"
        print row

jogador1 = Jogador("O")
jogador2 = Jogador("X")

tabuleiro = Tabuleiro()
tabuleiro.escrever(0)



