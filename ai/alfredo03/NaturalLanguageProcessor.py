class NaturalLanguageProcessor:
    pronouns = ["o que","quem","quando","onde","por que"]

    def normalize(self, question):        
        tokens = question.lower().split()
        tokens = self.groupPronoun(tokens)
        tokens = self.reduceTokens(tokens)
        normalizedQuestion = [] 
        pronoun = self.searchPronoun(tokens)
        normalizedQuestion.append(pronoun)
        normalizedQuestion = self.appendTokensExcept(pronoun, tokens, normalizedQuestion)
        return normalizedQuestion

    def groupPronoun(self, tokens):
        for index, token in enumerate(tokens):
            if (index-1) > 0:
                article = (tokens[index-1] == "o")
                if token == "que" and article:
                    tokens[index] = "o que"
                preposition = (tokens[index-1] == "por")
                if token == "que" and preposition:
                    tokens[index] = "por que"
        return tokens

    def reduceTokens(self, tokens):
        reducedTokens = []
        for token in tokens:
            if len(token) > 3:
                reducedTokens.append(token)
        return reducedTokens

    def searchPronoun(self,tokens):
        for token in tokens:
            if token in self.pronouns:
                return token
        return ""
        
    def appendTokensExcept(self, pronoun, inputTokens, outputTokens):
        for token in inputTokens:
            if token != pronoun:
                outputTokens.append(token)
        return outputTokens      
            
        
