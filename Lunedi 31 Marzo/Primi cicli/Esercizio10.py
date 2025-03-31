#ESERCIZIO 10
# creazione lista numeri
numeri = []
# ciclo per inserire 5 numeri
while True:
    print("Inserisci un numero")
    valore = input()
    if valore.lower() == "stop":
        break
    #converto il valore in intero
    num = int(valore)
    #aggiungo il numero alla lista
    numeri.append(num)   
#controllo se la lista e' vuota
if not numeri: #not numeri e' True se la lista e' vuota
    print("La lista e' vuota")
else:
    #trova il numero massimo di con ciclo for della lista
    massimo = numeri[0]
    for i in numeri:
        if i > massimo:
            massimo = i
    print("Il numero massimo e':", massimo)
# conteggio dei numeri nella lista
conteggio = 0
i=0
while i < len(numeri):
    conteggio += 1 # aumenta conteggio di 1
    i += 1 #aumenta i di 1
print("Il numero di elementi nella lista e':", conteggio)
