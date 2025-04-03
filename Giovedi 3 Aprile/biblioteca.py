from eser_classi2 import Libro

class Biblioteca:# Classe che rappresenta una biblioteca
    def __init__(self): # Inizializza la biblioteca con una lista vuota
        self.libri = []
    def aggiungi_libro(self, titolo, autore, pagine):# Aggiunge un libro alla biblioteca
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)
        return libro
    def rimuovi_libro(self, titolo):# Rimuove un libro dalla biblioteca
        libro_rimosso = None
        for libro in self.libri:
            if libro.titolo == titolo:
                libro_rimosso = libro
                break
        if libro_rimosso:
            self.libri.remove(libro_rimosso)
        return libro_rimosso
    def mostra_libri(self):# Mostra i libri presenti nella biblioteca
        if self.libri:
            print("Libri presenti nella biblioteca:")
            for libro in self.libri:
                print(f"{libro.titolo} - {libro.autore} - {libro.pagine} pagine")
        else:
            print("Nessun libro presente nella biblioteca.")
    def crea_libro(self): # Crea un libro da input
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        pagine = int(input("Inserisci il numero di pagine del libro: "))
        self.aggiungi_libro(titolo, autore, pagine)
    def stampa_libro(self, titolo):# Stampa le caratteristiche di un libro
        libro_trovato = None # Variabile per memorizzare il libro trovato
        for libro in self.libri:
            if libro.titolo == titolo:
                libro_trovato = libro
                break
        if libro_trovato:# Stampa le caratteristiche del libro trovato
            print(f"Titolo: {libro_trovato.titolo}")
            print(f"Autore: {libro_trovato.autore}")
            print(f"Numero di pagine: {libro_trovato.pagine}")
        else:
            print("Libro non trovato.")

def menu(): # Menu principale
    biblioteca = Biblioteca()
    while True:
        print("1. Aggiungi libro")
        print("2. Rimuovi libro")
        print("3. Mostra libri")
        print("4. Stampa libro")
        print("5. Esci")
        scelta = input("Scegli un'opzione (1-5): ")
        
        match scelta:
             case '1': # aggiungi libro
                 biblioteca.crea_libro()   
             case '2': # rimuovi libro
                 titolo = input("Inserisci il titolo del libro da rimuovere: ")
                 libro_rimosso = biblioteca.rimuovi_libro(titolo)
                 if libro_rimosso:
                     print("Libro rimosso con successo.")
                 else:
                     print("Libro non trovato.")    
             case '3': # mostra libri
                 biblioteca.mostra_libri()
                 
             case '4': # stampa libro
                 titolo = input("Inserisci il titolo del libro da stampare: ")
                 biblioteca.stampa_libro(titolo)   
             case '5': # esci
                 print("Arrivederci!")
                 break

menu() # Esegue il menu principale