from libro import Libro


    
class Libreria: # Classe per la libreria
    def __init__(self):
        self.catalogo = []
    def aggiungi_libro(self, libro): # Aggiunge un libro al catalogo
        if isinstance(libro, Libro):# Verifica se il libro è un oggetto Libro
            self.catalogo.append(libro)
    
    def rimuovi_libro(self, isbn):  # Rimuove un libro dal catalogo usando l'isbn
        self.catalogo = [libro for libro in self.catalogo if libro.isbn!=isbn] # Rimuove il libro dalla lista
    
    def cerca_per_titolo(self, titolo):# Cerca libri nel catalogo usando il titolo
        return [libro for libro in self.catalogo if libro.titolo==titolo] # Ritorna una lista dei libri con il titolo specificato
    
    def mostra_catalogo(self):# Stampa il catalogo completo
        if not self.catalogo:# Stampa un messaggio se il catalogo è vuoto
            print("Il catalogo è vuoto.")
        else:
            print("Catalogo Libreria: ")
            for libro in self.catalogo:
                print(f" {libro.descrizione()}") # Stampa le caratteristiche dei libri