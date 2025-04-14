import sqlite3

# Crea una connessione al database

mydb = sqlite3.connect('zoo.db')

# Creazione del cursor

mycursor = mydb.cursor()

# Creazione della tabella Animali

mycursor.execute('''CREATE TABLE IF NOT EXISTS Animali
                (ID INT PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Eta INT NOT NULL,
                Specie TEXT NOT NULL)
                ''')

# committa le modifiche

mydb.commit()

class Animale:
 def __init__(self, nome, eta):
    self.nome = nome
    self.eta = eta # Attributo per memorizzare l'età

 def parla(self):
    print(f"{self.nome} fa suono generico.") # Metodo di default per parlare

 def salva_in_db(self, specie):
     try:
         mycursor.execute(f"INSERT INTO Animali (Nome, Eta, Specie) VALUES (?,?,?)", (self.nome, self.eta, specie,))
         mydb.commit()
         print("Record aggiunto con successo")
     except sqlite3.Error as error:
         print("Error occurred:", error)

class Leone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Richiamo il costruttore della superclasse
    
    def parla(self):
        print(f"{self.nome}: roar!") # Override del metodo parla di Animale
    
    def caccia(self):
        print(f"{self.nome} sta cacciando nella savana.")
    
    def salva(self):
        self.salva_in_db("Leone")

class Giraffa(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Richiamo il costruttore della superclasse
    def parla(self):
        print(f"{self.nome}: mmmmmm!") # Override del metodo parla di Animale
    def mangia(self):
        print(f"{self.nome} sta mangiando delle  foglie.")
    def salva(self):
        self.salva_in_db("Giraffa")

class Pinguino(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Richiamo il costruttore della superclasse
    def parla(self):
        print(f"{self.nome}: cooo!") # Override del metodo parla di Animale
    def nuota(self):
        print(f"{self.nome} sta nuotando.")
    def salva(self):
        self.salva_in_db("Pinguino")

def stampa_tutti_animali(): # Funzione per stampare tutti gli animali presenti nel database
    mycursor.execute("SELECT * FROM Animali")
    for row in mycursor.fetchall():
        print(row)
def elimina_animali():
    mycursor.execute("DELETE FROM Animali")
    mydb.commit()
    print("Tutti gli animali sono stati eliminati.")

alex = Leone("Alex", 5)
alex.parla()
alex.caccia()
# alex.salva()

melman = Giraffa("Melman", 7)
melman.parla()
melman.mangia()
# melman.salva()

riko = Pinguino("Riko", 3)
riko.parla()
riko.nuota()
# riko.salva()

stampa_tutti_animali()

# elimina_animali()
# mycursor.execute("DELETE FROM sqlite_sequence WHERE name='Animali'")
# mydb.commit()