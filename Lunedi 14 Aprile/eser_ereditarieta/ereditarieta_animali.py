class Animale:
 def __init__(self, nome, eta):
    self.nome = nome
    self.eta = eta # Attributo per memorizzare l'età

 def parla(self):
    print(f"{self.nome} fa suono generico.") # Metodo di default per parlare

class Leone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Richiamo il costruttore della superclasse
    
    def parla(self):
        print(f"{self.nome}: roar!") # Override del metodo parla di Animale
    
    def caccia(self):
        print(f"{self.nome} sta cacciando nella savana.")

class Giraffa(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Richiamo il costruttore della superclasse
    def parla(self):
        print(f"{self.nome}: mmmmmm!") # Override del metodo parla di Animale
    def mangia(self):
        print(f"{self.nome} sta mangiando delle  foglie.")

class Pinguino(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta) # Richiamo il costruttore della superclasse
    def parla(self):
        print(f"{self.nome}: cooo!") # Override del metodo parla di Animale
    
    def nuota(self):
        print(f"{self.nome} sta nuotando.")

# Creazione di oggetti delle sottoclassi

alex = Leone("Alex", 5)
melman = Giraffa("Melman", 7)
riko = Pinguino("Riko", 3)

# Test delle sottoclassi

alex.parla() # Output: alex: roar!
melman.parla() # Output: melman: mmmmmm!
riko.parla() # Output: riko: cooo!

alex.caccia() # Output: alex sta cacciando.

melman.mangia() # Output: melman sta mangiando.

riko.nuota() # Output: riko sta nuotando.