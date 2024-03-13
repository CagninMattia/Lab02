import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while True:
    t.printMenu()
    txtIn = input().strip()

    if int(txtIn) == 1:
        inp = input("Ok, quale parola devo aggiungere?")
        uno, due = t.handleAdd(inp.lower())
        print(f"Fatto, aggiunto {uno} {due}")
    elif int(txtIn) == 2:
        inp = input("Ok, quale parola devo tradurre?")
        traduzione = t.handleTranslate(inp.lower())
        print(f"Traduzione: {traduzione}")
    elif int(txtIn) == 3:
        inp = input("Ok, quale parola vuoi tradurre? (massimo un ?)")
        traduzioni = t.handleWildCard(inp.lower())
        for el in traduzioni:
            print(f"Possibile traduione: {el}")
    elif int(txtIn) == 4:
        break
    else:
        raise ValueError("Numero incorretto")
