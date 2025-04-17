import numpy as np

matrice =np.random.randint(1, 101, size=(6, 6)) # Crea una matrice 6x6 con valori casuali tra 1 e 100
print("Matrice originale:\n", matrice)
print("Tipo di dati:", matrice.dtype) # Output: int64

sottomatrice = matrice[1:5, 1:5] # Estrae una sottomatrice 4x4
print("Sottomatrice:\n", sottomatrice)

inverti_righe = matrice[::-1] # Inverte le righe della matrice
print("Matrice con righe invertite:\n", inverti_righe)

indici = np.arange(inverti_righe.shape[0]) 
diagonale = inverti_righe[indici, indici] # Estrae la diagonale principale
print("Diagonale principale:\n", diagonale)

modificata = inverti_righe.copy() # Crea una copia della matrice invertita
modificata[modificata % 3 == 0] = -1 # Modifica gli elementi divisibili per 3 con -1
print("Matrice modificata:\n", modificata)