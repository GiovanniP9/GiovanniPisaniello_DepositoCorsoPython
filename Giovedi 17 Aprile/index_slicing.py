import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# # Indexing
# print(arr[0]) # Output: 1
# # Slicing
# print(arr[1:3]) # Output: [2 3]

# # Boolean Indexing
# print(arr[arr > 2]) # Output: [3 4 5]


# arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) 
# # Slicing sulle righe
# print(arr_2d[1:3]) # Output: [[ 5 6 7 8] 
#                             #[ 9 10 11 12]]
# # Slicing sulle colonne
# print(arr_2d[:, 1:3]) # Output: [[ 2 3]
#                       #          [ 6 7]
#                       #          [10 11]]
# # Slicing misto
# print(arr_2d[1:, 1:3]) # Output: [[ 6 7]
#                        #         [10 11]]

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# # Slicing di base
# print(arr[2:7]) # Output: [2 3 4 5 6]

# # Slicing con passo
# print(arr[1:8:2]) # Output: [1 3 5 7]
# # Omettere start e stop
# print(arr[:5]) # Output: [0 1 2 3 4]
# print(arr[5:]) # Output: [5 6 7 8 9]
# # Utilizzare indici negativi
# print(arr[-5:]) # Output: [5 6 7 8 9]
# print(arr[:-5]) # Output: [0 1 2 3 4]

arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices]) # Output: [20 40]
 
# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices]) # Output: [10 30 50]