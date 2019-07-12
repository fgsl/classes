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

    def escrever(self, casa, simbolo):
        if (self.casas[casa] == " "):
            self.casas[casa] = simbolo
        else:
            return False 
        row = " ___ ___ ___ \n"
        for i in range(0,9):
            row += "| " + self.casas[i] + " "
            if (((i+1) % 3) == 0):
                row += "|\n"
                row +=  "|___|___|___|\n"
        print row
        return True

    def fimDoJogo(self):
        fim = True
        for i in range(9):
            if (self.casas[i] == " "):
                fim = False
        return fim                   


simbolo = 0
while (simbolo <> 1 and simbolo <> 2):
    simbolo = int(raw_input("Jogador 1, escolhe O [1] ou X [2]?"))

jogador1 = Jogador("0" if simbolo == 1 else "X")
jogador2 = Jogador("X" if simbolo == 1 else "0")

tabuleiro = Tabuleiro()
vez = 1;
while (not tabuleiro.fimDoJogo()):
    if (vez == 1):
        jogador = jogador1
    else:
        jogador = jogador2
    casa = 0
    while (casa < 1 or casa > 9):
        casa = int(raw_input("Digite a casa, Jogador " + str(vez) + ":"))
    if (tabuleiro.escrever(casa-1, jogador.simbolo)):
        vez = (1 if vez == 2 else 2)
print "Fim do jogo"


