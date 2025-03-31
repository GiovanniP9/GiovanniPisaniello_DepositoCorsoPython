#esercizio 8 pari
#lista vuota per i numeri pari
numeri_pari = []

#ciclo per inserire 5 numeri
while len(numeri_pari) < 5:
     print("Inserisci un numero")
     num = int(input())
     #ciclo di controllo per vedere se il numero e' pari
     for i in range(2, num +1, 2): # uso range(2, num +1, 2) per controllare solo i numeri pari
        if i == num:
             numeri_pari.append(num)
             print("Il numero e' pari")
             break
     else:
         print("Il numero e' dispari")
print("I numeri pari inseriti sono:", numeri_pari)
    