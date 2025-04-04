#Prodotto
class Prodotto:
    # Questa classe rappresenta un prodotto con nome, costo e prezzo di vendita
    def __init__(self, nome, costo, p_vendita):
        self.nome = nome
        self.costo = costo
        self.p_vendita = p_vendita
    # Metodo per calcolare il profitto del prodotto
    def calcola_profitto(self):
        return self.p_vendita - self.costo
#Classe Fabbrica
class Fabbrica:
    def __init__(self):
        self.inventario = {} # Inizializza un dizionario vuoto per memorizzare i prodotti
    
    # Metodo per aggiungere un prodotto all'inventario
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario: # Controlla se il prodotto è già in inventario
            # Se il prodotto esiste già, aggiorna la quantità
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita # Aggiungi il prodotto all'inventario
        print(f"Aggiunto {quantita} di {prodotto.nome} all'inventario.")
    
    
    # Metodo per vendere un prodotto
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.inventario or self.inventario[prodotto.nome] < quantita: # Controlla se il prodotto è in inventario e se ci sono abbastanza unità
            print(f"Non ci sono abbastanza {prodotto.nome} in inventario.")
        else:# Se ci sono abbastanza unità, procedi con la vendita
            self.inventario[prodotto.nome] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Venduto {quantita} di {prodotto.nome}.")
            print(f"Profitto totale: {profitto} euro.")
            
    # Metodo per mostrare l'inventario        
    def mostra_inventario(self):
        if not self.inventario:# Controlla se l'inventario è vuoto
            print("L'inventario è vuoto.")
        else:# Se l'inventario non è vuoto, mostra i prodotti e le quantità
            print("Inventario attuale:")
            for nome, quantita in self.inventario.items():
                print(f"{nome}: {quantita} unità")
    
    # Metodo per gestire il reso di un prodotto           
    def reso_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.inventario:# Controlla se il prodotto è in inventario
            print(f"Il prodotto {prodotto.nome} non è presente in inventario.")
        else: # Se il prodotto è in inventario, procedi con il reso
            self.inventario[prodotto.nome] += quantita
            print(f"Reso {quantita} di {prodotto.nome}.")

# Funzione per il menu della fabbrica
# Questa funzione gestisce l'interfaccia utente per la gestione della fabbrica
def menu_fabbrica():
    fabbrica = Fabbrica()
    prodotti = {} # Inizializza un dizionario vuoto per memorizzare i prodotti
    
    
    while True:
        print("   Menu Fabbrica  ")
        print("1. Crea prodotto")
        print("2. Aggiungi prodotto")
        print("3. Vendi prodotto")
        print("4. Mostra inventario")
        print("5. Reso prodotto")
        print("6. Esci")
        scelta = input("Scegli un'opzione (1-6): ")
        
        match scelta:
            case '1':# Crea un nuovo prodotto
                nome = input("Inserisci il nome del prodotto: ")
                costo = float(input("Inserisci il costo del prodotto: "))
                p_vendita = float(input("Inserisci il prezzo di vendita del prodotto: "))
                nuovo_prodotto = Prodotto(nome, costo, p_vendita)
                prodotti[nome] = nuovo_prodotto # Aggiungi il prodotto al dizionario
                print(f"Prodotto {nome} creato con successo.")
            case '2': # Aggiungi un prodotto all'inventario
                nome = input("Inserisci il nome del prodotto da aggiungere: ")
                if nome not in prodotti: # Controlla se il prodotto esiste
                    # Se il prodotto non esiste, mostra un messaggio di errore
                    print(f"Il prodotto {nome} non esiste. Crealo prima.")
                    continue
                quantita = int(input("Inserisci la quantità da aggiungere: ")) #inserisci la quantità da aggiungere
                fabbrica.aggiungi_prodotto(prodotti[nome], quantita) # Aggiungi il prodotto all'inventario
            case '3': # Vendi un prodotto
                nome = input("Inserisci il nome del prodotto da vendere: ")
                if nome not in prodotti: # Controlla se il prodotto esiste
                    # Se il prodotto non esiste, mostra un messaggio di errore
                    print(f"Il prodotto {nome} non esiste.")
                    continue
                quantita = int(input("Inserisci la quantità da vendere: "))#inserisci la quantità da vendere
                fabbrica.vendi_prodotto(prodotti[nome], quantita)# Vendi il prodotto
            case '4':# Mostra l'inventario
                fabbrica.mostra_inventario()# Mostra l'inventario
            case '5':# Gestisci il reso di un prodotto
                nome = input("Inserisci il nome del prodotto da restituire: ")
                if nome not in prodotti:# Controlla se il prodotto esiste
                    # Se il prodotto non esiste, mostra un messaggio di errore
                    print(f"Il prodotto {nome} non esiste.")
                    continue
                quantita = int(input("Inserisci la quantità da restituire: "))#inserisci la quantità da restituire
                fabbrica.reso_prodotto(prodotti[nome], quantita)# Gestisci il reso del prodotto
            case '6':# Esci dal programma
                print("Arrivederci!")
                break
            case _:# Gestisci un'opzione non valida
                print("Opzione non valida. Riprova.")

# Esecuzione del menu della fabbrica
menu_fabbrica()
        
