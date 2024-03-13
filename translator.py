import dictionary
import re

def is_input_valid(input_string):
    # Utilizziamo una espressione regolare per controllare se l'input contiene solo lettere alfabetiche
    pattern = re.compile(r'^[a-zA-Z]+$')
    return bool(pattern.match(input_string))

class Translator:

    def __init__(self):
        self.diz = dictionary.Dictionary()

    def printMenu(self):
        print("Traduttore alieno-italiano\n")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self.diz.aggiungiDizionario(dict)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        alieno, *italiano = entry.lower().strip().split()
        if is_input_valid(alieno):
            bool = False
            for parola in italiano:
                if is_input_valid(parola) == False:
                    bool = True
            if bool == False:
                self.diz.addWord(alieno, italiano)
                return alieno, italiano
        else:
            raise ValueError("Porcaccio il tuo dio")

    def handleTranslate(self, query):
        if is_input_valid(query):
        # query is a string <parola_aliena>
            return self.diz.translate(query)
        else:
            raise ValueError("Porcaccio il tuo dio")

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        return self.diz.translateWordWildCard(query)
