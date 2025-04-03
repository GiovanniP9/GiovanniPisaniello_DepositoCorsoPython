from eser_classi1 import Punto
from eser_classi2 import Libro

class Gestore: # crea un oggetto Gestore con la lista dei punti e dei libri vuoti
    def __init__(self): # inizializza la lista dei punti e dei libri
        self.punti = []
        self.libri = []
    def aggiungi_punto(self, x, y):# aggiunge un punto alla lista dei punti
        punto = Punto(x, y)
        self.punti.append(punto)
        return punto
    def aggiungi_libro(self, titolo, autore, pagine):# aggiunge un libro alla lista dei libri
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)
    def mostra_punti(self):# stampa la lista dei punti creati dall'oggetto Gestore
        return self.punti
    def mostra_libri(self):# stampa la lista dei libri creati dall'oggetto Gestore
        return print(f" {self.libri}")

gestore = Gestore()# crea un oggetto Gestore
# aggiunge punti a gestore
x = int(input("Inserisci la coordinata x: "))
y = int(input("Inserisci la coordinata y: "))
gestore.aggiungi_punto(x, y)
x1 = int(input("Inserisci la coordinata x: "))
y1 = int(input("Inserisci la coordinata y: "))
gestore.aggiungi_punto(x1, y1)
# stampa la lista dei punti creati dall'oggetto Gestore
print(gestore.mostra_punti())
print()
# aggiunge libri a gestore
gestore.aggiungi_libro("Il Pianista", "Verdi", 100)
gestore.aggiungi_libro("La Divina Commedia", "Dante", 200)
# stampa la lista dei libri creati dall'oggetto Gestore
print(gestore.mostra_libri())