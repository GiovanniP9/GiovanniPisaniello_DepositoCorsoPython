# Classe base
class Animale:
 def __init__(self, nome):
    self.nome = nome

 def parla(self):
    print(f"{self.nome} fa suono generico.") # Metodo di default per parlare

# Classe derivata (eredita da Animale)
class Cane(Animale): # Classe derivata che eredita da Animale cosi da poter utilizzare i metodi e attributi della classe base
 def parla(self):
     print(f"{self.nome} abbaia!") # Override del metodo parla di Animale	
     
animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla() # Output: AnimaleGenerico fa suono generico.
cane.parla() # Output: Fido abbaia!