import numpy as np

array = np.random.randint(10, 51, size =20) # Crea un array di numeri interi casuali tra 10 e 50 di dimensione 20
print("Array originale:", array)
print("Tipo di dati:", array.dtype) # Output: int64

array_10 = array[:10] # Estrae i primi 10 elementi dell'array
print("Primi 10 elementi:", array_10)

array_ultimi_5 = array[-5:] # Estrae gli ultimi 5 elementi dell'array
print("Ultimi 5 elementi:", array_ultimi_5)
array_5_15 = array[5:15] # Estrae gli elementi dall'indice 5 all'indice 14 (15 escluso)
print("Elementi da 5 a 15 (escluso):", array_5_15)

array_ogni_3 = array[::3] # Estrae ogni terzo elemento dell'array
print("Ogni terzo elemento:", array_ogni_3)

array[5:10] = 99 # Modifica il valore dell'elemento all'indice 5 e 10
print("Array dopo la modifica:", array)