import random
#inserire un numero intero positivo
while True:
    n = int(input("Inserisci un numero intero positivo: "))
    if n > 0:
        break
    else:
        print("Il numero deve essere positivo. Riprova.")

#genera lista di numeri casuali tra 1 e n di lunghezza n
lista_numeri = []
for i in range(n+1): # Itera da 0 a n (incluso)
    # Aggiunge un numero casuale alla lista
    random_num = random.randint(1, n) # Genera un numero casuale tra 1 e n
    lista_numeri.append(random_num) # Aggiunge il numero casuale alla lista
# Stampa la lista di numeri casuali	
print("Lista di numeri casuali:", lista_numeri)

# blocco per calcolare e stampare la somma dei numeri pari nella lista
sommapari = 0
for i in lista_numeri:
    if i % 2 == 0: # Controlla se il numero è pari
        sommapari += i # Aggiunge il numero pari alla somma
print("La somma dei numeri pari nella lista è:", sommapari)

#blocco per stampare i numeri dispari nella lista
print("I numeri dispari nella lista sono:")
for i in lista_numeri:
    if i % 2 != 0: # Controlla se il numero è dispari
        print(i) # Stampa il numero dispari

#blocco per determinare se un numero è primo nella lista e stampare i numeri primi
for i in lista_numeri:
    if i > 1: # Controlla se il numero è maggiore di 1
        for j in range(2, int(i**0.5) + 1): # Controlla fino alla radice quadrata del numero
            if i % j == 0: # Se il numero è divisibile per j, non è primo
                print(i,"false.")
                break
        else:
            print(i, "True.")

#blocco per stampare i numeri primi nella lista
print("I numeri primi nella lista sono:")
for i in lista_numeri:
    if i > 1: # Controlla se il numero è maggiore di 1
        for j in range(2, int(i**0.5) + 1): # Controlla fino alla radice quadrata del numero
            if i % j == 0: # Se il numero è divisibile per j, non è primo
                break
        else:
            print(i) # Stampa il numero primo
            
#usa if per verificare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato
lista_sum=sum(lista_numeri) # Calcola la somma dei numeri nella lista
#controllare se la somma è un numero primo
if lista_sum > 1: # Controlla se la somma è maggiore di 1
    for j in range(2, int(lista_sum**0.5) + 1): # Controlla fino alla radice quadrata della somma
        if lista_sum % j == 0: # Se la somma è divisibile per j, non è primo
            primo = False
            break
    else:
        primo = True # La somma è un numero primo
# Stampa il risultato della verifica se la somma è un numero primo
print("La somma dei numeri nella lista è un numero primo?:", primo)
print("la somma è: ", lista_sum)

