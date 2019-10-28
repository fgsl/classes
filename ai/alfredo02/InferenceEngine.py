from KnowledgeBase import KnowledgeBase

class InferenceEngine:

    def __init__(self):
        self.knowledgeBase = KnowledgeBase()

    def answer(self, question):
        facts = self.knowledgeBase.getFacts(question)
        return question 
