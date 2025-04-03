#PRIME CLASSISE E METODI

class Automobile: # dichiaro la classe
    numero_di_ruote = 4 # attributo di classe
    numero_istanze = 0 # attributo di classe
    def __init__(self, marca, modello): # metodo costruttore
        self.marca = marca # attributo di istanza
        self.modello = modello # attributo di istanza
        Automobile.numero_istanze += 1 # incremento il numero di istanze di Automobile
    def stampa_info(self): # metodo di istanza
        print("L'automobile è una", self.marca, self.modello, self.numero_di_ruote)
    @classmethod
    def contare_automobili(cls):
        print(f"Sono state create {cls.numero_istanze} automobili.")

#sostituire mentalmente il self con la variabile che rappresenta l'oggetto stesso
Auto1 = Automobile("Fiat", "500") # crea un oggetto di Automobile
Auto2 = Automobile("BMW", "X3") # crea un altro oggetto di Automobile
Auto1.stampa_info() # stampa "L'automobile è una Fiat 500"
Auto2.stampa_info() # stampa "L'automobile è una BMW X3"
Auto1.numero_di_ruote = 6 # modifica il numero di ruote dell'auto1
print(Auto1.numero_di_ruote) # stampa 6
Automobile.contare_automobili() # Output: Sono state create 2 automobili.
print()

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome # Attributo per memorizzare il nome
        self.eta = eta # Attributo per memorizzare l'età
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")
        
# Creazione di un oggetto Persona
P = Persona("Pippo", 30)
print(P.nome) # Output: Pippo
print(P.eta) # Output: 30
P.saluta() # Output: Ciao, mi chiamo Pippo
print()

#METODO STATICO
class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b
# Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)
print(risultato) # Output: 8
print()

#METODO DI CLASSE
class Contatore:
    numero_istanze = 0 # Attributo di classe
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
        
# Creazione di alcune istanze
C1 = Contatore()
C2 = Contatore()
Contatore.mostra_numero_istanze()# Output: Sono state create 2 istanze.
print()

