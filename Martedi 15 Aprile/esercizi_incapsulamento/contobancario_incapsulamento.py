
class ContoBancario:# Classe per gestire i conti bancari
    def __init__(self,titolare):
        self.__titolare = None # Attributo privato per memorizzare il titolare
        self.set_titolare(titolare) # Chiamo il metodo per settare il titolare
        self.__saldo = 0.0 # Attributo privato per memorizzare lo saldo
    
    def deposita(self, importo): # Metodo per depositare un importo
        if isinstance(importo, (int, float)) and importo > 0:
            self.__saldo += importo # Aggiungo l'importo al saldo
            print(f"Deposito di importo {importo:.2f} eseguito con successo.")
        else:
            print("L'importo inserito non è valido.")
    
    def preleva(self, importo): # Metodo per prelevare un importo
        if not isinstance(importo, (int, float)) or importo <= 0:
            print("L'importo inserito non è valido.")
        elif importo > self.__saldo:
            print("Saldo insufficiente.")
        else:
            self.__saldo -= importo
            print(f"Prelievo di importo {importo:.2f} eseguito con successo.")
    
    def visualizza_saldo(self): # Metodo per visualizzare lo saldo del conto corrente
        return f"Saldo del conto corrente di {self.__titolare}: {self.__saldo:.2f}"
    
    def get_titolare(self): # Metodo per ottenere il titolare del conto corrente
        return self.__titolare
    
    def set_titolare(self, titolare):# Metodo per settare il titolare del conto corrente
        if isinstance(titolare, str) and titolare != "":
            self.__titolare = titolare
        else:
            print("Il titolare del conto non è valido.")
            
utenti = {} # Dizionario per memorizzare gli utenti con le loro password, variabile globale
def registra(): # Funzione per registrare un utente nel sistema
    print("\nRegistrazione nuovo utente")
    username = input("Scegli uno username: ").strip()
    password = input("Scegli una password: ").strip()

    if not username or not password:
        print("Username e password non possono essere vuoti.")
        return

    if username in utenti:
        print("Username già esistente.")
        return

    utenti[username] = password
    print("Registrazione completata con successo!")

def login(): # Funzione per eseguire il login dell'utente nel sistema
    print("\nLogin utente")
    tentativi = 3

    while tentativi > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if utenti.get(username) == password:
            print(f"Accesso consentito. Benvenuto, {username}!")
            return username
        else:
            tentativi -= 1
            print(f"Credenziali errate. Tentativi rimasti: {tentativi}")

    print("Troppi tentativi falliti. Uscita dal programma.")
    exit()
   
def menu_conto(): # Funzione per gestire il menu del conto corrente
    utente_loggato = None
    conto = None

    while True:
        if not utente_loggato:
            print("\n--- Benvenuto ---")
            print("1. Login")
            print("2. Registrati")
            print("0. Esci")

            scelta = input("Scegli un'opzione: ")

            match scelta:
                case "1": # Login
                    utente_loggato = login()
                    nome = input("Inserisci il nome del titolare del conto: ")
                    conto = ContoBancario(nome)
                case "2": # Registrazione
                    registra()
                case "0": # Uscita
                    print("Uscita dal programma.")
                    exit()
                case _: # Scelta non valida.
                    print("Scelta non valida.")
        else:
            print(f"\nBenvenuto {utente_loggato}, hai effettuato il login con successo!")
            print("\n--- Menu ---")
            print("1. Deposita")
            print("2. Preleva")
            print("3. Visualizza saldo")
            print("4. Mostra titolare")
            print("5. Cambia titolare")
            print("0. Esci")

            scelta = input("Scegli un'opzione: ")

            match scelta:
                case "1":# Deposita
                    try:
                        importo = float(input("Inserisci l'importo da depositare: "))
                        conto.deposita(importo)
                    except ValueError:
                        print("Inserisci un numero valido.")
                case "2":# Preleva
                    try:
                        importo = float(input("Inserisci l'importo da prelevare: "))
                        conto.preleva(importo)
                    except ValueError:
                        print("Inserisci un numero valido.")
                case "3":# Visualizza saldo
                    print(conto.visualizza_saldo())
                case "4":# Mostra titolare
                    print(f"Titolare: {conto.get_titolare()}")
                case "5":# Cambia titolare
                    nuovo_nome = input("Inserisci il nuovo nome del titolare: ")
                    conto.set_titolare(nuovo_nome)
                case "0":# Uscita
                    print("Uscita dal sistema. Grazie!")
                    break
                case _:# Scelta non valida.
                    print("Scelta non valida. Riprova.")
                    

menu_conto()