class Libro:
    def __init__ (self,titolo, autore, isbn): # Costruttore del libro
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self): # Metodo per descrivere il libro
        return f"Titolo: {self.titolo}, Autore: {self.autore}, (ISBN: {self.isbn})"