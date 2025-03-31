# esercizio 1 range

while True:
    scelta = input("Vuoi inserire un numero (s/n)? ")
    if scelta.lower() == 'n':
        valore = input("Inserisci un numero: ")
        if valore.isdigit(): #controllo se il valore e' un numero
            #converto il valore in intero
            numero = int(valore)
            if numero % 2 == 0:#controllo se il numero e' pari
                print("Il numero è pari")
            else:
                print("Il numero è dispari")
        else:
            print("Il valore inserito non è un numero valido")
    elif scelta.lower() == 's': #controllo se l'utente ha scelto di non inserire un numero
        print("Hai scelto di non inserire un numero")
        print("Inserisci una stringa")
        stringa = input()
        print("Hai inserito:", stringa)
        if len(stringa) %2 == 0: #controllo se la lunghezza della stringa e' pari
            print("La stringa è di lunghezza pari")
        else:#controllo se la lunghezza della stringa e' dispari
            print("La stringa è di lunghezza dispari")
    else:
        print("Scelta non valida. Riprova.")
    
    #chiedo se l'utente vuole continuare
    print("Vuoi continuare? (s/n)")
    risposta = input()	
    if risposta.lower() == 'n':
        break
print("Fine del programma")


        