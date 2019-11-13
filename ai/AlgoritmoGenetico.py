# coding: utf-8
import random

class AlgoritmoGenetico:
	tamanhoDaPopulacao = 0
	regras = None
	maximoDeIteracoes = 0	

	def __init__(self, tamanhoDaPopulacao, regras, maximoDeIteracoes):
		self.tamanhoDaPopulacao = tamanhoDaPopulacao
		self.regras = regras
		self.maximoDeIteracoes = maximoDeIteracoes
	

	def executar(self):
		# inicia população aleatoriamente
		populacao = [0] * self.tamanhoDaPopulacao
		for i,v in enumerate(populacao):
			populacao[i] = self.novoIndividuo()
		for i in range(0, self.maximoDeIteracoes):
			print "Iteração " + str(i) + "\n"
			individuosDaPopulacao = " ".join([str(elemento) for elemento in populacao])
			print "População: " + individuosDaPopulacao + "\n"
			novaPopulacao = []
			for j,v in enumerate(populacao):
				self.buscarPeloMelhorIndividuo(populacao[j])
				novaPopulacao.append(populacao[j])
			if novaPopulacao  == []:
				for j in enumerate(populacao):
					populacao[j] = self.novoIndividuo()
			while len(novaPopulacao) < self.tamanhoDaPopulacao:
				novaPopulacao.append(self.crossover(populacao))
			for j in enumerate(novaPopulacao):	
				novaPopulacao[j] = self.mutacao(novaPopulacao[j])
			populacao = novaPopulacao
		melhorIndividuo = None
		for individuo in populacao:
		    self.buscarPeloMelhorIndividuo(individuo)
		if melhorIndividuo == null:
			print "Não obteve êxito \n"
	
	def mutacao(self, individuo):
		if random.randint( 0, 10 ) % 2 == 0:
			individuo = self.novoIndividuo()
		return individuo
	
	def crossover(self, populacao):
		return self.regras.crossover(populacao, self.regras.nvalores)
	
	def novoIndividuo(self):
		individuo = []
		for i in range(0, self.regras.nvalores):
			individuo.append(self.regras.randomValue())
		return individuo
	
	def buscarPeloMelhorIndividuo(self, individuo):
	    melhorIndividuo = self.regras.obterMelhorIndividuo(individuo)
	    if melhorIndividuo != None:
	        print "\n" + ('=' * 80)
	        print "\nMelhor solução: " + self.regras.mostrarIndividuo(melhorIndividuo) + "\n"
	        print "\n" + ('=' * 80) + "\n"
	        exit()
	    return melhorIndividuo
