

""" eta = input("inserisci la tua eta: ")
if eta.isdigit():
    print("la tua eta e' ", 2025-eta)
else:
    print("non hai inserito un numero") """

""" valore ="buongiorno a tutti"
valore = valore.replace("buongiorno", "buon pomeriggio") #sostituisce la stringa "buongiorno" con "buon pomeriggio"
print(valore) """

""" valore = "buongiorno a tutti"
lista = valore.split(" ") #crea una lista di stringhe separate da uno spazio
print(lista) #stampa la lista """

""" lista = ["buongiorno", "a", "tutti"]
del lista[-1] #elimina l'ultimo elemento della lista
#trasforma la lista in una stringa
valore = " ".join(lista) #unisce gli elementi della lista in una stringa separati da uno spazio
print(valore) #stampa la stringa """

""" stringa = "tommaso giovanni alfredo"
lista = ["tommaso", "giovanni", "alfredo"]
print(stringa.count("tommaso")) #conta il numero di volte che compare la stringa "tommaso"
print("tommaso" in stringa) #controlla se la stringa "tommaso" e' presente nella stringa
print("tom" in stringa) #controlla se la stringa "tom" e' presente nella stringa 
print("tommaso" in lista) #controlla se la stringa "tommaso" e' presente nella lista
print("tom" in lista) #controlla se la stringa "tom" e' presente nella lista """
# """ 
# """ lista = ["tommaso", "giovanni", "alfredo"]
# lista2 = []

# """ for i in lista: #ciclo for per scorrere la lista
#     if "m" in i:
#         lista2.append(i) #aggiunge alla lista2 gli elementi che contengono la lettera "m"
# print(lista2) #stampa la lista2
#  """
# lista2 = [i for i in lista if "m" in i] #list comprehension per creare la lista2 e vuole dire che per ogni i in lista se "m" e' in i allora aggiungi i alla lista2
# print(lista2) #stampa la lista2 """

# tupla = ("tommaso", "giovanni", "alfredo") #crea una tupla
# #tupla2 = tuple(lista) #trasforma la lista in una tupla 
# set1 = {"tommaso", "giovanni", "alfredo"} #crea un set
# set2 = set(tupla) #trasforma la tupla in un set

#DIZIONARI

# cliente1 = {"nome": "tommaso", "cognome": "russo", "eta": 25} #crea un dizionario
# cliente2 = {"nome": "giovanni", "cognome": "russo", "eta": 30} #crea un dizionario
# clienti = {1: cliente1, 2: cliente2} #crea un dizionario di dizionari	

# print(clienti[1]["nome"]) #stampa il nome del cliente 1
# for n in clienti: #ciclo for per scorrere il dizionario clienti
#     print(clienti[n]["nome"]) #stampa il nome del cliente n
#     print(clienti[n]["cognome"]) #stampa il cognome del cliente n
#     print(clienti[n]["eta"]) #stampa l'eta' del cliente n

# for n in clienti: #ciclo for per scorrere il dizionario clienti
#     for i in n.values():
#         print(i) #stampa i valori del dizionario n

# # per velocizzare
# for n in clienti:
#     for i in clienti[n]:
#         print(clienti[n][i]) #stampa i valori del dizionario n

# lista = [clienti[n][i] for n in clienti for i in clienti[n]] #list comprehension per creare la lista dei valori del dizionario clienti
# print(lista) #stampa la lista dei valori del dizionario clienti

# for k,value in cliente1.items(): #ciclo for per scorrere il dizionario cliente1
#     print(f"chiave: {k},valore:  {value}") #stampa la chiave e il valore del dizionario cliente1

# print(cliente1.get("nome", "valore non presente")) #stampa il valore della chiave "nome" del dizionario cliente1, se non presente stampa "valore non presente"
# print(cliente1.setdefault("via", "valore non presente")) #stampa il valore della chiave "via" del dizionario cliente1, se non presente aggiunge la chiave "via" con il valore "valore non presente"
# print(cliente1.keys()) #stampa le chiavi del dizionario cliente1
# print(cliente1) #stampa il dizionario cliente1

# cliente1M = {k+"M":v+"M" for k,v in cliente1.items()} #crea un nuovo dizionario cliente1M con le chiavi e i valori del dizionario cliente1 + "M"
# print(cliente1M) #stampa il dizionario cliente1M

# lista = ["zero" , "uno", "due", "tre"]

# for indice, valore in enumerate(lista): #ciclo for per scorrere la lista con l'indice
#     print(indice, valore) #stampa l'indice e il valore della lista

