class Dictionary:
    def __init__(self):
        self.diz = {}

    def aggiungiDizionario(self, dizionario):
        with open(dizionario) as diz:
            for line in diz.readlines():
                alieno, italiano = line.strip().split()
                self.diz[alieno] = italiano

    def addWord(self, alieno, italiano):
        for parola in italiano:
            if alieno in self.diz:
                if parola not in self.diz[alieno]:
                    self.diz[alieno].append(parola)
            else:
                self.diz[alieno] = []
                self.diz[alieno].append(parola)

    def translate(self, alieno):
        var = self.diz.get(alieno)
        return var

    def translateWordWildCard(self, parola_cercata):
        risultati = []
        for chiave, valore in self.diz.items():
            if len(chiave) == len(parola_cercata):
                corrisponde = True
                for char1, char2 in zip(chiave, parola_cercata):
                    if char1 != char2 and char2 != "?":
                        corrisponde = False
                        break
                if corrisponde:
                    risultati.append((chiave, valore))
        return risultati

    def ritornaDiz(self):
        return self.diz
