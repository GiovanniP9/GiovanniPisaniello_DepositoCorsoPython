#Indovina il numero
import random

def genera_numero():
    return random.randint(1, 100)

def gestione_tentativi(numero):
    tentativi = 0
    while True:
        tentativo = input("Indovina il numero: ")
        
        if tentativo == 'exit':
            print("Hai deciso di chiudere il programma. il numero era: ")
            print(numero)
            break
        #controllo numero valido
        if tentativo.isdigit():
            tentativo= int(tentativo) #trasforma tentativo in numero intero
            tentativi += 1
            if tentativo < numero:
               print("Il numero che devi indovinare è maggiore. Riprova!")
            elif tentativo > numero:
                print("Il numero che devi indovinare è minore. Riprova!")
            else:
                print("Hai indovinato, numero di tentativi: ")
                print(tentativi)
                break
        
def gioco():
    
    numero_random= genera_numero()
    print("Benvenuto nel gioco")
    print("Per uscire digita exit")
    
    gestione_tentativi(numero_random)

#avvia gioco
gioco()
            
                        
