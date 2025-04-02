#LISTE
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomi = ["Alice", "Bob", "Charlie", "David"]
misto = [1,"due", True, 4.5]

print(numeri)
print(numeri[0]) # 1
print(numeri[2]) # 3
print(numeri[5]) # 6
print(numeri[9]) # 10
print(numeri[4]) # 5

numeri[2] = 100
print(numeri) # [1, 2, 100, 4, 5, 6, 7, 8, 9, 10]

nomi[2] = "Giovanni"
print(nomi) # ['Alice', 'Bob', 'Giovanni', 'David']

misto[2] = False
print(misto) # [1, 'due', False, 4.5]

#METODI LISTE
numeri1 = [1, 2, 3, 4, 5]
print(len(numeri1)) # 5
numeri1.append(2) # Aggiunge 2 alla fine della lista
print(numeri1) # [1, 2, 3, 4, 5, 2]
numeri1.insert(2, 10) # Inserisce 10 alla posizione 2
print(numeri1) # [1, 2, 10, 3, 4, 5, 2]
numeri1.remove(2) # Rimuove il primo elemento uguale a 2
numeri1.sort() # Ordina la lista
print(numeri1) # [1, 2, 3, 4, 5, 10]

numeri1.sort(reverse=True) # Ordina la lista in ordine decrescente
print(numeri1) # [10, 5, 4, 3, 2, 1]

numeri1.count(5) # Conta il numero di volte che 5 appare nella lista
numeri1.index(4) # Restituisce l'indice del primo elemento uguale a 4
numeri1.pop(2) # Rimuove l'elemento alla posizione 2

#TUPLE
punto = (3, 4)
print(punto[0]) # Output: 3
print(punto[1]) # Output: 4

#INSIEMI

set1 = set([1, 2, 3, 4, 5]) # Inizializza un insieme
set2 = {4, 5, 6, 7, 8} # Inizializza un insieme

print(set1) # Output: {1, 2, 3, 4, 5}

print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5} si basa sull'intersezione dei due insiemi
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8} si basa sull'unione
