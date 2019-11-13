# coding: utf-8
import random

class Regras:
	nvalores = 5
#=================================================
	def obterMelhorIndividuo(self,individuo):
		melhorIndividuo = None
		suficiente = self.fitness (individuo)
		if (suficiente < 15):
			if (suficiente > 12):
				melhorIndividuo = individuo
		return melhorIndividuo
#=================================================
	def fitness(self,x):
		W = x[0]* 12 + x[1] * 1 + x[2] * 4 + x[3] * 1 + x[4] * 2
		print "\nSomatório do peso:\n"
		print "x[0]* 12 + x[1] * 1 + x[2] * 4 + x[3] * 1 + x[4] * 2 = W\n"
		V = x[0]* 4 + x[1] * 2 + x[2] * 10 + x[3] * 1 + x[4] * 2
		print "\nSomatório do valor:\n"
		print "x[0]* 4 + x[1] * 2 + x[2] * 10 + x[3] * 1 + x[4] * 2 = V\n"
		return W
#=================================================
	def crossover(self, populacao):
		novoIndividuo = [0] * self.nvalores
		for i in enumerate(self.nvalores):
			novoIndividuo[i] =  ( int ) ((populacao [i][0] + end ( populacao[i] )) / 2)			
		return novoIndividuo
#=================================================
	def mostrarIndividuo(self, individuo):
	    x = individuo
	    return "x[0] = " + str(x[0]) + ",x[1] = " + str(x[1]) + ", x[2] = " + str(x[2]) + ", x[3] = " + str(x[3]) +", x[4] = " + str(x[4])
#=================================================	
	def randomValue(self):
	    return random.randint(0,3)
