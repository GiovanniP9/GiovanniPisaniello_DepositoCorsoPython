# ESERCIZIO RIASSUNTIVO
# Programma che incorpora gli argomenti studiati fino ad ora

# 1. Cos'è Python?
def cosa_e_python():
    print("Python è un linguaggio di programmazione interpretato, orientato agli oggetti, dinamico e ad alto livello. rilasciato nel 1991. ")
    print("interpretato vuol dire che nel momento che mandiamo in esecuzione non compila subito")
    print("IL CREATORE DI PYTHON È GUIDO VAN ROSSUM. LUI SI ANNOIAVA A SCRIVERE IN C E HA CREATO PYTHON. E QUINDI CREA UN LINGUAGGIO PER PROGRAMMATORI.")

print()

# 2. UML (Unified Modeling Language)
def uml():
    print("UML o Unified Modeling Language è uno standard de facto per la modellazione di software ed è uno strumento grafico.")
    print("L'UML è standardizzato ossia è uguale ovunque lo usi seppure con regole personalizzate.")
    print("L'UML ha come caratteristica la visuale ossia utilizza diagrammi per rappresentare concettualmente e fisicamente gli elementi e le interazioni.")
    print("L'UML è polivalente ossia non è limitato a software OOP ossia OBJECT ORIENTED PROGRAMMING.")
    print("L'UML è estensibile ossia è personalizzabile quindi si può adattare ad esigenze specifiche.")

print()

#3. Uso di print()
#print viene usato per stampare a video i valori
def uso_di_print():
    print("Questo è un esempio di print:")
    print("print viene usato per stampare a video i valori")

print()

# 4. uso di input()
def uso_di_input():
    print("Questo è un esempio di input:")
    nome = input("Inserisci il tuo nome: ") #input viene usato per ricevere input da tastiera
    print("Il tuo nome è:", nome)

print()

# 5. Commenti in Python
# I commenti in Python iniziano con il simbolo # e questo ne è un esempio
"""	
QUESTO INVECE È UN COMMENTO SU
PIÙ LINEE

"""

# 6. Tipi di dato
def tipi_di_dato():
# Python supporta diversi tipi di dato
    print("Tipi di dato in Python:")
    print("1. Numeri interi (int): 10, -5, 0")
    print("2. Numeri decimali (float): 3.14, -2.71")
    print("3. Stringhe (str): 'ciao', 'Python'")
    print("4. Booleani (bool): True, False")
    numero = int(input("Inserisci un numero intero: ")) # int è un tipo di dato per gli interi
    stringa = input("Inserisci una stringa: ") # str è un tipo di dato per le stringhe

print()
# 7. OPERATORI LOGICI E STRUTTURE DI CONTROLLO IF-ELIF-ELSE
def operatore_logici_e_strutture_di_controllo():
    #ESEMPIO
    numero = int(input("Inserisci un numero: "))
    if numero > 0: # if è una struttura di controllo che verifica se una condizione è vera
        print("Il numero è positivo")
        print("Il numero è pari:", numero % 2 == 0)
        print("Il numero è dispari:", numero % 2!= 0)
    # Abbiamo vari tipo di operatori logici
    # tra cui: - AND (e) - OR (o) - NOT (non)
    if numero > 0 and numero % 2 == 0: 
        print("Il numero è positivo e pari")
    elif numero > 0 or numero % 2 == 0: # ELIF è una struttura di controllo che viene usata quando abbiamo più di un'opzione
        print("Il numero è positivo o pari")
    else: # ELSE è una struttura di controllo che viene usata quando non si verifica nessuna delle altre condizioni
        print("Il numero non è positivo o pari")

print()

# 8. Liste
def liste():
    lista_numeri = [1, 2, 3, 4, 5] # una lista è un tipo di dato per gli array
    lista_elementi = ["ciao", "Python", 10, 3.14, True] # una lista può contenere elementi di diversi tipi
    #una lista può essere vuota
    lista_vuota = []
    #una lista ha diversi metodi
    lista_numeri.append(6) # aggiunge un elemento alla fine della lista
    lista_numeri.insert(2, 7) # aggiunge un elemento in una posizione specifica
    lista_elementi.remove("Python") # rimuove il primo elemento uguale a "Python"
    conta_lista = len(lista_numeri) # conta quanti elementi ci sono nella lista
    print("La lista di numeri è:", lista_numeri)
    print("La lista di elementi è:", lista_elementi)
print()

# 9. Match
def match_case():
# match è una struttura di controllo che viene usata quando abbiamo più condizioni uguali simile allo switch di Java
 print("match è una struttura di controllo che viene usata quando abbiamo più condizioni uguali simile allo switch di Java")
 numero = int(input("Inserisci un numero: "))
 match numero:
     case 1:
            print("Hai inserito 1.")
     case 2:
            print("Hai inserito 2.")
     case _: # default è una struttura di controllo che viene eseguita quando non viene trovata una condizione corrispondente
            print("Numero non riconosciuto nel match-case.")


print()

# 10. uso di while e range

def uso_di_while_e_range():
    i = 1

    while i <= 10: # finche i sarà minore o uguale a 10 sara vera
        print("stampa numero:", i)
        i += 1
    
    print("range() è una funzione incorporata in Python che restituisce una sequenza di numeri interi che possono essere utilizzati in cicli for o in altre situazioni in cui è necessario iterare su un insieme di valori. ")
    for i in range(1, 6): 
        print(i)


print()
    
# 11. Funzioni
# le funzioni sono un modo per organizzare il codice in modo efficiente e riutilizzabile
def somma(a, b):
    print("È stata richiama la funzione somma")
    return a + b

# print("La somma di 3 e 5 è:", somma(3, 5)) # Chiamo la funzione
