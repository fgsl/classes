# coding: utf-8
import os

os.system("cls" if "windows" in os.name.lower() else "clear")

resposta = raw_input("\nOlá, eu sou Alfredo. Em que posso ajudá-lo?\n")

print "\nVocê disse: " + resposta

while (True):
    resposta = raw_input("\nPosso ajudá-lo em mais alguma coisa?\n")
    if ("não" in resposta.lower()):
        break

print "\nObrigado e até logo\n\n"
 


