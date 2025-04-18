
# def funzione (a, b=0): #metto b=0 per permettere di passare solo un argomento a funzione, quando si passa due argomenti viene automaticamente utilizzato il secondo argomento
#     valore= a+b
#     print(valore)
#     return valore

# altrovalore = funzione (10, 11)
# print(altrovalore)

# def funzione (*args): #args è una tupla di argomenti
#     print(args)

# funzione(10, 20, 30, 40) #passo più argomenti tramite una tupla

# def funzione (*args):
#     for el in args: #itero sui singoli elementi della tupla
#         print(el)
        
# funzione(10, 20, 30, 40) #passo più argomenti tramite una tupla

# def funzione(**args):# in questo caso args è un dizionario
#     print(args["nome"])#accesso all'elemento "nome" del dizionario
    
# funzione(nome="Giorgio", cognome="Pisaniello", eta=32) #passo più argomenti tramite un dizionario

# eta = 38 #creo una variabile globale
# def funzione():
#     global eta #uso la variabile globale
#     eta += 1
#     print(eta)
# funzione() #stampa eta

# lista = [1, 2, 3, 4, 5]
# def funzione(a):
#     return a * 2 #funzione che ritorna il quadrato di un numero

# utilizzo la funzione con la lista

# for numero in range(len(lista)):  #itero sui singoli elementi della lista:
#     #modifica elemento della lista con la funzione
#     lista[numero] = funzione(lista[numero]) #il numero viene passato come argomento alla funzione

# print(lista) #stampo la lista modificata

#map è una funzione built-in che applica una funzione ad ogni elemento di una lista 
#utilizzo map che applica la funzione alla lista
# lista =list(map(funzione, lista)) #uso la funzione map per applicare la funzione alla lista

# lista = [1, 2, 3, 4, 5]

# def pari(a):
#     return a % 2 == 0 #funzione che ritorna True se il numero è pari
# lista2 = []
# for i in lista:
#     if pari(i):
#         lista2.append(i) #aggiungo il numero pari alla nuova lista
# print(lista2) #stampo la lista dei numeri pari
        
#utilizzo filter che applica la funzione alla lista
# filter è una funzione built-in che applica una funzione a tutti gli elementi di una lista e restituisce una nuova lista con gli elementi che soddisfano la condizione
# pari_lista = list(filter(pari, lista)) #uso la funzione filter per applicare la funzione alla lista
# print(pari_lista) #stampo la lista dei numeri pari

# lista = [1, 2, 3, 4, 5]

# stringa = '-'.join(lista) # non va perche che la lista contiene elementi di tipo diverso
# print(stringa) #stampo la lista concatenata con un trattino

#utilizzo la funzione map per convertire i numeri in stringhe
# stringhe_lista = list(map(str, lista))
# stringa = '-'.join(stringhe_lista)
# print(stringa) #stampo la lista concatenata con un trattino

#utilizzo la funzione map per convertire i numeri in stringhe e riordinare i risultati

#MODULI PYTHON
# import random ma cosi importo tutta la libreria
#inoltre per richiamare una funzione dall'altra libreria uso il nome della libreria seguito dal nome della funzione
# se facciamo import random as r: #aggiungiamo un alias per random
#se vogliamo solo un metodo dalla libreria possiamo scrivere
# from random import randint
#randit() senza usare il nome della libreria

#try e except per gestire eccezioni

#try: # codice che potrebbe generare un'eccezione
#except viene eseguito quando un'eccezione viene generata
# a = 0
# try:
#     print(8 / a)
# except ValueError as e: # con ValueError posso specificare solo per il valore
#     print("l'errore è nel valore")
# except ZeroDivisionError as e: #con ZeroDivisionError posso specificare solo per la divisione per zero
#     print("L'errore è:", e)
# except:
#     print("ERRORE sconosciuto") # posso specificare un'eccezione generica
# print ("proseguo con il resto del codice")

# CSV
# a intende appendere i dati dal file
# r intende leggere i dati dal file
# x intende scrivere i dati nel file

# def scrittura(metodo,stringa):
#     with open('prova.txt', 'a') as file:
#          file.write(stringa)
# scrittura("w", 'Ciao, ')

# def lettura(): #lettura dei dati dal file
#     with open('prova.txt', 'r') as file:
#         contenuto = file.read()
#     return contenuto

# print(lettura())

# clienti = [["nome","cognome","via"],
#            ["Giorgio","Pisaniello","Via Roma 12"],
#            ["Giuseppe","Rossi","Via Milano 34"]]
# righe =[]
# for riga in clienti:
#     righe.append(",".join(riga))
# file = "\n".join(righe)