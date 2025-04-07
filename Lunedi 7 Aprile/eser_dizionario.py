from collections import Counter

stringa = input("Inserisci una stringa: ")
dizionario = {}

# for lettera in stringa: # per ogni lettera nella stringa 
#     dizionario[lettera] = dizionario.get(lettera, 0) + 1 # se la lettera e' presente nel dizionario, incrementa il valore di 1, altrimenti aggiungi la lettera con valore 1

# print(dizionario)

# conteggio = Counter(stringa) # crea un oggetto Counter a partire dalla stringa

# dizionario  = dict(conteggio) # crea un dizionario a partire da un oggetto Counter

# print(dizionario)

# for i in stringa: # per ogni lettera nella stringa
#     dizionario[i] =stringa.count(i) # conta il numero di volte che compare la lettera nella stringa e aggiungi la lettera con il valore del conteggio

for lettera in stringa: # per ogni lettera nella stringa
    if lettera in dizionario:
        dizionario[lettera] += 1 # incrementa il valore di 1
    else:
        dizionario[lettera] = 1 # aggiungi la lettera con valore 1

print(dizionario)