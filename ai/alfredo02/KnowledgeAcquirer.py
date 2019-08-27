from KnowledgeEngineer import KnowledgeEngineer
from MachineLearner import MachineLearner
import config

class KnowledgeAcquirer:
   def __init__(self):
       self.knowledgeSource = config.getKnowledgeSource()

   def getFacts(self, question):
       return self.knowledgeSource.getFacts(question)
