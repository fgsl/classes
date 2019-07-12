# jogo da velha
# coding: utf-8
class Jogador:
    vencedor = 0;

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
        for i in [0,3,6]:
            if (self.casas[i] != " " and self.casas[i] == self.casas[i+1] and self.casas[i+1] == self.casas[i+2]):
                Jogador.vencedor = (1 if self.casas[i] == jogador1.simbolo else 2)
                return True;
        for i in [0,1,2]:
            if (self.casas[i] != " " and self.casas[i] == self.casas[i+3] and self.casas[i+3] == self.casas[i+6]):
                Jogador.vencedor = (1 if self.casas[i] == jogador1.simbolo else 2)
                return True;
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
print "Não houve vencedor" if Jogador.vencedor == 0 else "O vencedor foi o Jogador " + str(Jogador.vencedor)


