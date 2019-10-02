from KnowledgeBase import KnowledgeBase
from NaturalLanguageProcessor import NaturalLanguageProcessor

class InferenceEngine:

    def __init__(self):
        self.knowledgeBase = KnowledgeBase()
        self.nlp = NaturalLanguageProcessor()

    def answer(self, question):
        normalizedQuestion = self.nlp.normalize(question)
        facts = self.knowledgeBase.getFacts(normalizedQuestion)
        return facts 
