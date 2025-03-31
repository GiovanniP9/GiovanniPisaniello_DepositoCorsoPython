
print("Menu:")
print("1. numeri pari o dispari")
print("2. conto alla rovescia")
print("3. stampare quadrato di una lista")
print("4. esercizio 10")
print("5. esci")

selezione = int(input("Seleziona da 1 a 5: "))
    
match selezione:
    case 1:
            #PUNTO 1 CONTROLLO NUMERO PARI O DISPARI

            #inserire numero
            num = int(input("Inserisci un numero: "))
            #controllo se il numero e' pari o dispari
            if num % 2 == 0:
                print("Il numero e' pari")
            else:
                print("Il numero e' dispari")
    case 2:
         #PUNTO 2 CONTO ALLA ROVESCIA INFINITO CON WHILE
        #ciclo infinito
        while True:
            #inserire numero per conto alla rovescia
                num = int(input("Inserisci numero positivo per conto alla rovescia: "))
                if num < 0:
                    print("Il numero deve essere positivo")
                    continue #torna all'inizio del ciclo
            #ciclo di conto alla rovescia
                for i in range(num, -1, -1):
                    print(i)
                print("Fine conto alla rovescia")
    case 3:
            #PUNTO 3 STAMPARE IL QUADRATO DI UNA LISTA DI NUMERI
            #lista vuota per i numeri
            numeri = []
            #ciclo per inserire 5 numeri
            for i in range(5):
                num = int(input("Inserisci un numero: "))
                numeri.append(num)
            #ciclo per stampare il quadrato dei numeri
            for i in numeri:
                print("Il quadrato di", i, "e' ", i**2)
    case 4:
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