import numpy as np

# # Creazione di un array
# arr = np.array([1, 2, 3, 4, 5])
# # Utilizzo di alcuni metodi
# print("Forma dell'array:", arr.shape) # Output: (5,) shape restituisce la forma dell'array, che in questo caso è un array unidimensionale con 5 elementi
# print("Dimensioni dell'array:", arr.ndim) # Output: 1 ndim indica il numero di dimensioni dell'array
# print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma) dtype indica il tipo di dati degli elementi dell'array
# print("Numero di elementi:", arr.size) # Output: 5 size indica il numero totale di elementi nell'array
# print("Somma degli elementi:", arr.sum()) # Output: 15 sum calcola la somma degli elementi
# print("Media degli elementi:", arr.mean()) # Output: 3.0 mean calcola la media degli elementi
# print("Valore massimo:", arr.max()) # Output: 5 max calcola il valore massimo
# print("Indice del valore massimo:", arr.argmax()) # Output: 4 argmax restituisce l'indice del valore massimo dell'array
# print("Valore minimo:", arr.min()) # Output: 1 min calcola il valore minimo
# print("Indice del valore minimo:", arr.argmin()) # Output: 0 argmin restituisce l'indice del valore minimo dell'array

#Creazione di un array bidimensionale con obbligo dtype
# arr = np.array([1, 2, 3], dtype='int32')
# print(arr.dtype) # Output: int32

#uso di arange per creare un array di numeri interi
# arr = np.arange(10)
# print(arr) # Output: [0 1 2 3 4 5 6 7 8 9]

#uso di reshape per cambiare la forma dell'array
arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr) # Output: [[0 1 2] [3 4 5]]