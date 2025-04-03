
class Libro:
    def __init__(self, titolo, autore, pagine): # Costruttore del libro
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    def descrizione(self): # Metodo per descrivere il libro
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Pagine: {self.pagine}"
    def __repr__(self): # Metodo per ritornare una stringa di rappresentazione dell'oggetto
        return f"Libro(titolo='{self.titolo}', autore='{self.autore}', pagine={self.pagine})"

if __name__ == "__main__":
    # Creazione di due oggetti Libro
    Libro1 = Libro("Il Pianista", "Giuseppe Verdi", 150)
    Libro2 = Libro("La Divina Commedia", "Dante", 231)
    # Stampa la descrizione dei due libri
    print("Il libro ha come " +Libro1.descrizione())
    print("Il libro ha come " +Libro2.descrizione())
