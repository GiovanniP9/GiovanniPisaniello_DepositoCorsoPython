
class MetodoPagamento:
    def effettua_pagamento(self, importo): # Metodo da implementare nelle sottoclassi
        print("Metodo di pagamento generico")

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):# Metodo specifico per la carta di credito
        print(f"Pagamento di {importo:.2f} effettuato con carta di credito.")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):# Metodo specifico per PayPal
        print(f"Pagamento di {importo:.2f} effettuato con PayPal.")
class Bonifico(MetodoPagamento):
    def effettua_pagamento(self, importo):# Metodo specifico per bonifico
        print(f"Pagamento di {importo:.2f} effettuato con bonifico.")

class Gestorepagamenti:
    def __init__(self, metodo):# Inizializza il gestore con un metodo di pagamento
        self.metodo = metodo

    def paga(self, importo):# Metodo per effettuare il pagamento
        self.metodo.effettua_pagamento(importo)# Effettua il pagamento utilizzando il metodo specifico

def menu():
    # Mostra il menu di scelta del metodo di pagamento
    print("Scegli un metodo di pagamento:")
    print("1. Carta di credito")
    print("2. PayPal")
    print("3. Bonifico")
    scelta = input("Inserisci la tua scelta (1-3): ")
    
    match scelta:
        case "1":
            metodo = CartaDiCredito()
        case "2":
            metodo = PayPal()
        case "3":
            metodo = Bonifico()
        case _:
            print("Scelta non valida.")
            return None
    try: # Controlla se l'importo è valido
        importo = float(input("Inserisci l'importo da pagare: "))
        if importo <= 0:
            print("L'importo deve essere maggiore di zero.")
    except ValueError:
        print("Inserisci un numero valido.")
    
    gestore = Gestorepagamenti(metodo)
    gestore.paga(importo)
menu()
