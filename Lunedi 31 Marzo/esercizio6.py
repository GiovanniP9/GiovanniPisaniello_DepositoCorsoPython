#esercizio 6

#chiedi all'utente di inserire due numeri
num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero: "))

#chiedi all'utente di inserire un operatore
operatore = input("inserisci l'operatore (+, -, *, /,**): ")

#ciclo di controllo per vedere se l'operatore e' valido
if operatore == "+": #somma
    risultato = num1 + num2
elif operatore == "-": #sottrazione
    risultato = num1 - num2
elif operatore == "*": #moltiplicazione
    risultato = num1 * num2
elif operatore == "/": #divisione
    if num2 != 0: #controllo se il secondo numero e' zero
        risultato = num1 / num2
    else:
        risultato = "impossibile dividere per zero"
elif operatore == "**": #potenza
    #controllo se il secondo numero e' negativo
    if num2 < 0:
        risultato = "impossibile calcolare la potenza con esponente negativo"
    else:
        #calcolo la potenza
        risultato = num1 ** num2
else:
    risultato = "operatore non valido"
#stampa il risultato
print("il risultato e':", risultato)