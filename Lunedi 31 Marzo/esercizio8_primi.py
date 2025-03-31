#esercizio 8 primi
#lista vuota per i numeri primi
numeri_primi = []

#ciclo per inserire 5 numeri
while len(numeri_primi) < 5:
        print("Inserisci un numero")
        num = int(input())
        #ciclo di controllo per vedere se il numero e' primo
        if num <= 1:
            print("Il numero non e' primo")
        else:
            for i in range(2, num):
                if num % i == 0:
                    print("Il numero non e' primo")
                    break
            else:
                numeri_primi.append(num)
                print("Il numero e' primo")
print("I numeri primi inseriti sono:", numeri_primi)