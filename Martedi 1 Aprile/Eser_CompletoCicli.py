
while True:
    # Chiede all'utente di inserire un numero
    n = int(input("Inserisci un numero (0 per terminare): "))
    if n == 0: # Se l'utente inserisce 0, esci dal ciclo
        print("Hai inserito 0, il programma termina.")
        break
#blocco per calcolare la somma dei numeri pari da 2 a n
# Inizializza la somma a zero
sommapari = 0
for i in range (2, n+1, 2):
    sommapari += i
print("La somma dei numeri pari da 2 a", n, "è:", sommapari)
#blocco per stampare i numeri dispari da 1 a n
print("I numeri dispari da 1 a", n, "sono:")
for i in range (1, n+1, 2):
    print(i) # Stampa il numero corrente
#blocco per verificare se n è primo
if n > 1:
    for i in range(2, int(n**0.5) + 1): # Controlla fino alla radice quadrata di n
        if n % i == 0: # Se n è divisibile per i, non è primo
            print(n, "non è un numero primo.")
            break
    else:
        print(n, "è un numero primo.")
else:
    print(n, "non è un numero primo.")