import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GiFeTe251098?",
  database="squadre"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE IF NOT EXISTS squadre; USE squadre;")

mycursor.execute("""CREATE TABLE IF NOT EXISTS membri_squadra (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    eta INT NOT NULL
    );""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS giocatori (
    id INT AUTO_INCREMENT PRIMARY KEY,
    membro_id INT,
    ruolo VARCHAR(50) NOT NULL,
    numero_maglia INT NOT NULL,
    FOREIGN KEY (membro_id) REFERENCES membri_squadra(id) ON DELETE CASCADE
    );
    """)

mycursor.execute("""CREATE TABLE IF NOT EXISTS Allenatori (
    id INT AUTO_INCREMENT PRIMARY KEY,
    membro_id INT,
    anni_di_esperienza INT,
    FOREIGN KEY (membro_id) REFERENCES membri_squadra(id) ON DELETE CASCADE
    );
    """)

mycursor.execute("""CREATE TABLE IF NOT EXISTS Assistenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    membro_id INT,
    specializzazione VARCHAR(100),
    FOREIGN KEY (membro_id) REFERENCES membri_squadra(id) ON DELETE CASCADE
    );
    """)
mydb.commit()

#CLASSI

class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    def salva(self):
        mycursor.execute("INSERT INTO membri_squadra (nome, eta) VALUES (%s, %s)", (self.nome, self.eta))
        mydb.commit()
        self.id = mycursor.lastrowid # Salvo l'id del membro per creare i giocatori
        return self.id
    def descrivi(self):
        print(f"Nome: {self.nome}, Eta: {self.eta}")

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    def salva(self):
        membro_id = super().salva()
        mycursor.execute("INSERT INTO giocatori (membro_id, ruolo, numero_maglia) VALUES (%s, %s, %s)", (membro_id, self.ruolo, self.numero_maglia))
        mydb.commit()

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza
    def salva(self):
        membro_id = super().salva()
        mycursor.execute("INSERT INTO allenatori (membro_id, anni_di_esperienza) VALUES (%s, %s)", (membro_id, self.anni_di_esperienza))
        mydb.commit()
    def dirige_allenamento(self):
        descrizione = input(f"come {self.nome} dirige l'allenamento? ")
        print(f"{self.nome} dirige l'allenamento cosi: {descrizione}")

class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
    def salva(self):
        membro_id = super().salva()
        mycursor.execute("INSERT INTO Assistenti (membro_id, specializzazione) VALUES (%s, %s)", (membro_id, self.specializzazione))
        mydb.commit()
    
    def supporta_team(self):
        descrizione = input(f"come {self.nome} supporta il team? ")
        print(f"{self.nome} supporta il team cosi: {descrizione}")

# INPUT GIOCATORI
def aggiungi_giocatori():
    num_giocatori = int(input("Quanti giocatori vuoi aggiungere? "))
    for i in range(num_giocatori):
        nome = input(f"Nome giocatore {i+1}: ")
        eta = int(input(f"Età giocatore {i+1}: "))
        ruolo = input(f"Ruolo giocatore {i+1}: ")
        numero_maglia = random.randint(1, 99)
        giocatore = Giocatore(nome, eta, ruolo, numero_maglia)
        giocatore.salva()
        print(f"Giocatore {nome} aggiunto con successo!")

def aggiungi_allenatori():
    nome = input("Nome allenatore: ")
    eta = int(input("Età allenatore: "))
    anni_di_esperienza = int(input("Anni di esperienza allenatore: "))
    allenatore = Allenatore(nome, eta, anni_di_esperienza)
    allenatore.salva()
    allenatore.dirige_allenamento()
    print(f"Allenatore {nome} aggiunto con successo!")

def aggiungi_assistenti():
    nome = input("Nome assistente: ")
    eta = int(input("Età assistente: "))
    specializzazione = input("Specializzazione assistente: ")
    assistente = Assistente(nome, eta, specializzazione)
    assistente.salva()
    assistente.supporta_team()
    print(f"Assistente {nome} aggiunto con successo!")

def partita():
    mycursor.execute("SELECT g.id FROM giocatori g")
    giocatori_ids = [row[0] for row in mycursor.fetchall()] # Salvo gli id dei giocatori per creare le partite
    if len(giocatori_ids) < 10:
        print("Devi aggiungere almeno 10 giocatori per iniziare una partita!")
        return
    random.shuffle(giocatori_ids) # Riordino gli id per creare le due squadre a caso
    squadra1 = giocatori_ids[:5]
    squadra2 = giocatori_ids[5:10]
    
    ################################
            #da rivedere
    # print("\nSquadra 1:")
    # for giocatore in squadra1:
    #     print(f"- {giocatore[1]}")
    # print("\nSquadra 2:")
    # for giocatore in squadra2:
    #     print(f"- {giocatore[1]}")
    ################################
        
    mycursor.execute("SELECT m.nome FROM allenatori a JOIN membri_squadra m ON a.membro_id = m.id")
    allenatori = [row[0] for row in mycursor.fetchall()]
    random.shuffle(allenatori)
    if len(allenatori) >= 2:
        print(f"\nAllenatore squadra 1: {allenatori[0]}")
        print(f"Allenatore squadra 2: {allenatori[1]}")

    mycursor.execute("SELECT m.nome FROM assistenti ass JOIN membri_squadra m ON ass.membro_id = m.id")
    assistenti = [row[0] for row in mycursor.fetchall()]
    random.shuffle(assistenti)
    if len(assistenti) >= 2:
        print(f"Assistente squadra 1: {assistenti[0]}")
        print(f"Assistente squadra 2: {assistenti[1]}")
    
    punteggio_squadra1 = sum(random.choice([0,1]) for _ in squadra1)
    punteggio_squadra2 = sum(random.choice([0,1]) for _ in squadra2)
    print(f"Punteggio squadra 1: {punteggio_squadra1}")
    print(f"Punteggio squadra 2: {punteggio_squadra2}")
    if punteggio_squadra1 > punteggio_squadra2:
        print("La squadra 1 ha vinto!")
    elif punteggio_squadra1 < punteggio_squadra2:
        print("La squadra 2 ha vinto!")
    else:
        print("Pareggio!")

def menu():
    while True:
        print("\nMenu:")
        print("1. Aggiungi giocatori")
        print("2. Aggiungi allenatore")
        print("3. Aggiungi assistente")
        print("4. Inizia partita")
        print("5. Esci")
        scelta = int(input("Scelta: "))
        
        match scelta:
            case 1:
                aggiungi_giocatori()   
            case 2:
                aggiungi_allenatori()    
            case 3:
                aggiungi_assistenti()    
            case 4:
                partita()   
            case 5:
                print("Arrivederci!")
                break

menu()
mydb.close()


