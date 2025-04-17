import numpy as np

array = np.arange(10, 50) # Crea un array di numeri interi da 10 a 49
print("Array originale:", array)

#verifica il tipo di dati dell'array
print("Tipo di dati:", array.dtype) # Output: int64 

#cambia il tipo di dati dell'array in float
array_float = np.array(array, dtype='float64') # Cambia il tipo di dati in float64
print("tipo di dati:", array_float.dtype) # Output: float64
print("Array con tipo di dati float:", array_float)

#stampa forma dell'array
print("Forma dell'array:", array.shape) # Output: (40,) indica che l'array è unidimensionale con 40 elementi
