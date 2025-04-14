from libro import Libro
from libreria import Libreria

def menu(): # Menu principale
    mia_libreria = Libreria()
  
    while True:
        print("\n===== MENU LIBRERIA =====")
        print("1. Aggiungi un libro")
        print("2. Rimuovi un libro (per ISBN)")
        print("3. Cerca libri per titolo")
        print("4. Mostra catalogo")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        match scelta:
            case '1': # Aggiunta di un libro
                print("Inserisci i dati del libro:")
                titolo = input("Titolo del libro: ")
                autore = input("Autore del libro: ")
                isbn = input("ISBN del libro: ")
                nuovo_libro = Libro(titolo, autore, isbn) # Crea un nuovo libro e lo aggiunge alla libreria
                mia_libreria.aggiungi_libro(nuovo_libro)
                
            case '2':
                print("Inserisci l'ISBN del libro da rimuovere:")
                isbn = input("ISBN del libro da rimuovere: ")
                mia_libreria.rimuovi_libro(isbn) # Rimuove il libro dalla libreria usando l'ISBN
            case '3': # Cerca libri per titolo
                titolo = input("Titolo del libro per cui cercare: ")
                libri = mia_libreria.cerca_per_titolo(titolo)# Cerca i libri usando il titolo e li stampa
                if libri:
                    print("Libri trovati: ", len(libri))
                    for libro in libri:
                        print(f" - Descrizione: {libro.descrizione()}")
                else:# Se non trova libri con il titolo
                    print("Nessun libro trovato con questo titolo.")
            case '4':# Mostra catalogo dei libri
                print("Catalogo dei libri:")
                mia_libreria.mostra_catalogo()
            case '5':# Esci
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida. Riprova.")
menu() # Esegue il menu principale