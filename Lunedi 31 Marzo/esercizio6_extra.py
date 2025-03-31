# esercizio 6 extra

while True:
    print("Menu operazioni:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. combinazione di operazioni")
    print("6. Uscita")
    
    scelta = input("Scegli un'operazione (1-6): ")
    
    # creazione di un dizionario per le operazioni
    match scelta:
        case '1': #somma
            num1 = int(input("Inserisci il primo numero: "))
            num2 = int(input("Inserisci il secondo numero: "))
            risultato = num1 + num2
            print("Il risultato della somma è:", risultato)
        case '2': #sottrazione
            num1 = int(input("Inserisci il primo numero: "))
            num2 = int(input("Inserisci il secondo numero: "))
            risultato = num1 - num2
            print("Il risultato della sottrazione è:", risultato)
        case '3': #moltiplicazione
            num1 = int(input("Inserisci il primo numero: "))
            num2 = int(input("Inserisci il secondo numero: "))
            risultato = num1 * num2
            print("Il risultato della moltiplicazione è:", risultato)
        case '4': #divisione
            num1 = int(input("Inserisci il primo numero: "))
            num2 = int(input("Inserisci il secondo numero: "))
            if num2 != 0:
                risultato = num1 / num2
                print("Il risultato della divisione è:", risultato)
            else:
                print("Impossibile dividere per zero")
        case '5': #combinazione di operazioni
            num1 = int(input("Inserisci il primo numero: "))
            num2 = int(input("Inserisci il secondo numero: "))
            operatore1 = input("Inserisci il primo operatore (+, -, *, /): ")
            operatore2 = input("Inserisci il secondo operatore (+, -, *, /): ")
            # applico il primo operatore
            if operatore1 == "+":
                risultato = num1 + num2
            elif operatore1 == "-":
                risultato = num1 - num2
            elif operatore1 == "*":
                risultato = num1 * num2
            elif operatore1 == "/":
                if num2 != 0:
                    risultato = num1 / num2
                else:
                    risultato = "Impossibile dividere per zero"
            else:
                risultato = "Operatore non valido"
            # ora applico il secondo operatore   
            if operatore2 == "+":
                risultato += num2
                print("Il risultato della combinazione di operazioni è:", risultato)
            elif operatore2 == "-":
                risultato -= num2
                print("Il risultato della combinazione di operazioni è:", risultato)
            elif operatore2 == "*":
                risultato *= num2
                print("Il risultato della combinazione di operazioni è:", risultato)
            elif operatore2 == "/":
                if num2 != 0:
                    risultato /= num2
                    print("Il risultato della combinazione di operazioni è:", risultato)
                else:
                    risultato = "Impossibile dividere per zero"
            else:
                risultato = "Operatore non valido"
        #uscita dal ciclo
        case '6':
            print("Uscita dal programma.")
            break