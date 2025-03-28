# CREDENZIALI PREDEFINITE

username_predefinito = "admin"
password_predefinito = "12345"

domanda1 = "leone"
domanda2 = "pizza"

#INPUT CREDENZIALI
username = input("Inserisci il tuo nome utente: ")
password = input("Inserisci la tua password: ")

if username == username_predefinito and password == password_predefinito:
    # Se l'utente ha inserito le credenziali corrette
    print("seleziona una domanda di sicurezza:")
    print("1. Qual'è il nome del tuo animale domestico?")
    print("2. Qual'è il tuo cibo preferito?")
    scelta_domanda = int(input("scegli un opzione: "))
    if scelta_domanda == 1: #domanda 1
        # Se l'utente ha selezionato la domanda 1
        risposta = input("Rispondi alla domanda di sicurezza: Qual'è il nome del tuo animale domestico? ")
        if risposta == domanda1: 
            print("Accesso riuscito!")
            print("Benvenuto nel sistema di gestione utenti!")           
        else:
            print("Accesso negato! Risposta errata.")
            exit()
    else: #domanda 2
        # Se l'utente ha selezionato la domanda 2
        risposta = input("Rispondi alla domanda di sicurezza: Qual'è il tuo cibo preferito? ")
        if risposta == domanda2:
            print("Accesso riuscito!")
            print("Benvenuto nel sistema di gestione utenti!")           
        else:
            print("Accesso negato! Risposta errata.")
            exit()
    # Se l'utente ha inserito le credenziali corrette       
    print("vuoi modificare le credenziali?")
    print("1. si")	
    print("2. no")
    scelta = int(input("scegli un opzione: "))
    match scelta:
        case 1: #modifica credenziali
            username = input("inserisci il tuo nuovo nome utente: ")
            password = input("inserisci la tua nuova password: ")
            print("Credenziali modificate con successo!")
        case 2: #non modificare credenziali
            print("Credenziali non modificate.")
        case _: #opzione non valida
            print("Opzione non valida.")
    
else:
    print("Accesso negato! Nome utente o password errati.")
    exit()
