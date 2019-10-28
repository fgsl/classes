from KnowledgeAcquirer import KnowledgeAcquirer
import json

class KnowledgeBase:

    def __init__(self):
        self.knowledgeAcquirer = KnowledgeAcquirer()
        self.facts = []

    def getFacts(self, question):
        self.facts = self.getKnownFacts(question)
        if (self.facts == []): 
            self.facts = self.knowledgeAcquirer.getFacts(question)
        return self.facts

    def getKnownFacts(self,question):
        f = open("facts.json", "r")
        facts = json.load(f)
        key = ''.join(question)
        if key in facts:
            return [facts[key]]
        return []
