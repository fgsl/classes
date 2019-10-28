# coding: utf-8
from InferenceEngine import InferenceEngine
from UserInterface import UserInterface

class Alfredo:
    def __init__(self):
        self.ui = UserInterface()
    
    def atender(self):
        questao = self.ui.ask("Olá, eu sou Alfredo. Em que posso ajudar?")
        self.ui.say("Você disse: " + questao)
        ie = InferenceEngine()
        fatos = ie.answer(questao);
        self.ui.say("".join(fatos))
        while (True):
            questao = self.ui.ask("Posso ajudar em mais alguma coisa?")
            if ("não" in questao.lower()):
                break
            self.ui.say(ie.answer(questao))
        self.ui.say("Obrigado e até logo")

