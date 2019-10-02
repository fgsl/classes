import os
class UserInterface:
    
    def __init__(self):
        os.system("cls" if "windows" in os.name.lower() else "clear")
    
    def ask(self, question):
        return raw_input("\n" + question + "\n")
        
    def say(self, text):
        print "\n" + text + "\n"