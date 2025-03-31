numeri = []

# menu principale
while True:
    print("Menu:")
    print("1. Inserisci un numeri")
    print("2. trova numero massimo")
    print("3. conta numeri")
    print("4. mostra lista")
    print("5. esci")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1": # inserimento numeri
       print("Inserisci numeri uno alla volta. Digita 'Stop' per terminare. ")
       while True:
        valore = input("Inserisci numero: ")
        if valore.lower() == "stop": # termina l'inserimento
            break
        numeri.append(int(valore))
    elif scelta == "2": # trova numero massimo
         massimo = numeri[0]
         for num in numeri:
             if num > massimo:
                 massimo = num
         print("Numero massimo: ")
         print(massimo)
    elif scelta == "3": # conta numeri
        conteggio = 0
        for num in numeri:
            conteggio += 1
        print("Numero di elementi nella lista: ")
        print(conteggio)
    elif scelta == "4": # mostra lista
        print("Lista dei numeri: ")
        for num in numeri:
            print(num)
    elif scelta == "5": # esci
        print("Uscita dal programma")
        break
    else:
        print("Scelta non valida, riprova.")
