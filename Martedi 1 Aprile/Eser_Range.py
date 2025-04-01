
N = int(input("Inserisci un numero: ")) # Numero da cui partire
step = int(input("Inserisci il passo: "))# Passo da saltare
# Stampa i numeri da 0 a N con il passo specificato
for i in range(0, N + 1, step):
    print(i) # Stampa il numero corrente