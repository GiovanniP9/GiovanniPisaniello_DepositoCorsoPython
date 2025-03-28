# Esercizio 1
# Scrivere un programma che chiede all'utente di inserire un numero e stampa un messaggio in base al numero inserito.
numero = int(input("Inserisci un numero: ")) # Chiede all'utente di inserire un numero
if numero > 0: # Controlla se il numero è maggiore di 0
    print("sei nel primo livello") # Stampa un messaggio se il numero è positivo
    numero = int(input("Inserisci un altro numero: ")) # Chiede all'utente di inserire un altro numero
    if numero < 0: # Controlla se il numero è minore di 0
        print("sei nel secondo livello")
        numero = int(input("Inserisci un altro numero: "))
        if numero == 0: # Controlla se il numero è uguale a 0
            print("sei nel terzo livello")
        else: # Se il numero non è uguale a 0
             print("numero diverso da zero")
    else: # Se il numero non è minore di 0
        print("numero non negativo")
else: # Se il numero non è maggiore di 0
    print("numero non positivo")

