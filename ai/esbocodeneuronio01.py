# coding: utf-8
x = [1,0,1,0,2,0] # entradas
w = [5,9,11,4,2,58] # pesos

soma = 0
i = 0
while (i<6):
    soma += x[i] * w[i]
    i = i + 1

if (soma > 50):
   print "Está doendo!"


