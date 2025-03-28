# esercizio 3

Lista_utenti = []

print("Benvenuto nel sistema di registrazione utenti!")
print("hai gia un account?")
print("1. si")
print("2. no")
scelta = int(input("scegli un opzione: "))
if scelta == 2: #crea un nuovo utente
    nome = input("inserisci il tuo nome: ")
    password = input("inserisci la tua password: ")
    
    id = len(Lista_utenti) + 1
    
    nuovo_utente = [id, nome, password]
    Lista_utenti.append(nuovo_utente)
    print("Utente registrato con successo!")
# else:
    #controllo se l'utente esiste già
#    nome = input("inserisci il tuo nome: ")
#    password = input("inserisci la tua password: ")