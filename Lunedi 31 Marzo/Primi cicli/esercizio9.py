#PUNTO 1 CONTROLLO NUMERO PARI O DISPARI

#inserire numero
num = int(input("Inserisci un numero: "))
#controllo se il numero e' pari o dispari
if num % 2 == 0:
    print("Il numero e' pari")
else:
    print("Il numero e' dispari")
    
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
    
    #ciclo di controllo per ripetere il conto alla rovescia
    risposta = input("Vuoi ripetere? (s/n): ")
    if risposta == "n":
        break

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