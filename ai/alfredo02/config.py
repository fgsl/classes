import KnowledgeEngineer
import MachineLearner

def getKnowledgeSource():
    configFile = open(os.getcwd() + "/alfredo02/knowledgesource.config","r");
    sourceSelected = configFile.read()    
    configFile.close()
    if (sourceSelected == "KnowledgeEngineer"):
        instance = KnowledgeEngineer()
    if (sourceSelected == "MachineLearner"):
        instance = MachineLearner()     
    return instance;
