import mysql.connector

def connessione_db():
    # Connessione al database MySQL
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="GiFeTe251098?",  # Cambia con la tua password
        database="scuoladb"
    )

class Persona:
    def __init__(self, nome, eta ):
        self.__nome = nome
        self.__eta = eta
    def get_nome(self):
        return self.__nome
    def get_eta(self):
        return self.__eta
    def set_nome(self, nome):
        self.__nome = nome
    def set_eta(self, eta):
        self.__eta = eta
    
    def presentazione(self):
        print(f"Nome: {self.__nome}, Eta: {self.__eta}")
        
    def salva(self, cursor):
        # Salva la persona nel database
        cursor.execute("INSERT INTO Persona (nome, eta) VALUES (%s, %s)", (self.__nome, self.__eta))
        return cursor.lastrowid  # Restituisce l'ID appena inserito

class Studente(Persona):
        def __init__(self, nome, eta, voti):
          super().__init__(nome, eta)
          self.__voti = voti
      
        def get_voti(self):
          return self.__voti
        def set_voti(self, voti):
          self.__voti = voti
      
        def __media_voti(self):
          if not self.__voti:
              return 0
          return sum(self.__voti) / len(self.__voti)
        def presentazione(self):
          media = self.__media_voti()
          print(f"Ciao sono: {self.get_nome()}, ho: {self.get_eta()} anni e la mia media voti è di: {media:.2f}")
        def salva(self, cursor):
            persona_id = super().salva(cursor)
            voti_str = ",".join(map(str, self.__voti))
            cursor.execute("INSERT INTO Studente (persona_id, voti) VALUES (%s, %s)", (persona_id, voti_str))

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
    def get_materia(self):
        return self.__materia
    def set_materia(self, materia):
        self.__materia = materia
    def presentazione(self):
          print(f"Salve sono: {self.get_nome()}, ho: {self.get_eta()} anni e sono il professore di: {self.__materia}")
    def salva(self, cursor):
        persona_id = super().salva(cursor)
        cursor.execute("INSERT INTO Professore (persona_id, materia) VALUES (%s, %s)", (persona_id, self.__materia))

class Scuola:
    def __init__(self, nome):
        self.__nome = nome
        self.__studenti = []
        self.__professori = []
        
    def aggiungi_studente(self, studente):
        if isinstance(studente, Studente):
            self.__studenti.append(studente)
    def aggiungi_professore(self, professore):
        if isinstance(professore, Professore):
            self.__professori.append(professore)
    def stampa_studenti(self):
        print(f"Elenco studenti nella scuola {self.__nome}:")
        for studente in self.__studenti:
            studente.presentazione()
    def stampa_professori(self):
        print(f"Elenco professori nella scuola {self.__nome}:")
        for professore in self.__professori:
            professore.presentazione()
    def salva_scuola_db(self, cursor):
        # Inserisce la scuola nel database (facoltativo, solo se desideri avere una scuola nel DB)
        cursor.execute("INSERT INTO Scuola (nome) VALUES (%s)", (self.__nome,))
        return cursor.lastrowid

    
def crea_tabelle(cursor):
    # Crea il database se non esiste
    cursor.execute("CREATE DATABASE IF NOT EXISTS scuoladb;")
    cursor.execute("USE ScuolaDB;")

    # Crea la tabella Persona
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Persona (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            eta INT NOT NULL
        );
    """)

    # Crea la tabella Studente
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studente (
            id INT AUTO_INCREMENT PRIMARY KEY,
            persona_id INT,
            voti TEXT,
            FOREIGN KEY (persona_id) REFERENCES Persona(id)
        );
    """)

    # Crea la tabella Professore
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Professore (
            id INT AUTO_INCREMENT PRIMARY KEY,
            persona_id INT,
            materia VARCHAR(255) NOT NULL,
            FOREIGN KEY (persona_id) REFERENCES Persona(id)
        );
    """)


def menu():
    mydb = connessione_db()
    cursor = mydb.cursor()
    
    crea_tabelle(cursor)
    
    scuola = Scuola("Scuola di Informatica")
    while True:
        print("1. Aggiungi studente")
        print("2. Aggiungi professore")
        print("3. Stampa studenti")
        print("4. Stampa professori")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                nome = input("Nome studente: ")
                eta = int(input("Età: "))
                voti_input = input("Inserisci i voti separati da virgola (es. 7,8,9): ")
                voti = [int(v) for v in voti_input.split(",") if v.strip().isdigit()]
                studente = Studente(nome, eta, voti)
                scuola.aggiungi_studente(studente)
                studente.salva(cursor)
                print("Studente aggiunto.")

            case "2":
                nome = input("Nome professore: ")
                eta = int(input("Età: "))
                materia = input("Materia insegnata: ")
                professore = Professore(nome, eta, materia)
                scuola.aggiungi_professore(professore)
                professore.salva(cursor)
                print("Professore aggiunto.")

            case "3":
                scuola.stampa_studenti()

            case "4":
                scuola.stampa_professori()

            case "5":
                print("Uscita dal programma.")
                mydb.commit() #salva le modifiche nel database
                mydb.close()
                break

menu()