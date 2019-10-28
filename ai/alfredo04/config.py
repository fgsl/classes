import KnowledgeEngineer
import MachineLearner

import os

def getKnowledgeSource():
    configFile = open(os.getcwd() + "/alfredo04/knowledgesource.config","r");
    sourceSelected = configFile.read()    
    configFile.close()
    if (sourceSelected.strip() == "KnowledgeEngineer"):
        return KnowledgeEngineer.KnowledgeEngineer()
    if (sourceSelected.strip() == "MachineLearner"):
        return MachineLearner()     
    return KnowledgeEngineer();
