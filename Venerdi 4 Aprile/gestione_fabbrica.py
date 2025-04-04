#Prodotto
class Prodotto:
    def __init__(self, nome, costo, p_vendita):
        self.nome = nome
        self.costo = costo
        self.p_vendita = p_vendita
    
    def calcola_profitto(self):
        return self.p_vendita - self.costo
#Classe Fabbrica
class Fabbrica:
    def __init__(self):
        self.inventario = {} # Inizializza un dizionario vuoto per memorizzare i prodotti
    
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
        print(f"Aggiunto {quantita} di {prodotto.nome} all'inventario.")
    
    
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.inventario or self.inventario[prodotto.nome] < quantita:
            print(f"Non ci sono abbastanza {prodotto.nome} in inventario.")
        else:
            self.inventario[prodotto.nome] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Venduto {quantita} di {prodotto.nome}.")
            print(f"Profitto totale: {profitto} euro.")
    def mostra_inventario(self):
        if not self.inventario:
            print("L'inventario è vuoto.")
        else:
            print("Inventario attuale:")
            for nome, quantita in self.inventario.items():
                print(f"{nome}: {quantita} unità")
                
    def reso_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.inventario:
            print(f"Il prodotto {prodotto.nome} non è presente in inventario.")
        else:
            self.inventario[prodotto.nome] += quantita
            print(f"Reso {quantita} di {prodotto.nome}.")

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
            case '1':
                nome = input("Inserisci il nome del prodotto: ")
                costo = float(input("Inserisci il costo del prodotto: "))
                p_vendita = float(input("Inserisci il prezzo di vendita del prodotto: "))
                nuovo_prodotto = Prodotto(nome, costo, p_vendita)
                prodotti[nome] = nuovo_prodotto # Aggiungi il prodotto al dizionario
                print(f"Prodotto {nome} creato con successo.")
            case '2':
                nome = input("Inserisci il nome del prodotto da aggiungere: ")
                if nome not in prodotti:
                    print(f"Il prodotto {nome} non esiste. Crealo prima.")
                    continue
                quantita = int(input("Inserisci la quantità da aggiungere: "))
                fabbrica.aggiungi_prodotto(prodotti[nome], quantita) # Aggiungi il prodotto all'inventario
            case '3':
                nome = input("Inserisci il nome del prodotto da vendere: ")
                if nome not in prodotti:
                    print(f"Il prodotto {nome} non esiste.")
                    continue
                quantita = int(input("Inserisci la quantità da vendere: "))
                fabbrica.vendi_prodotto(prodotti[nome], quantita)
            case '4':
                fabbrica.mostra_inventario()
            case '5':
                nome = input("Inserisci il nome del prodotto da restituire: ")
                if nome not in prodotti:
                    print(f"Il prodotto {nome} non esiste.")
                    continue
                quantita = int(input("Inserisci la quantità da restituire: "))
                fabbrica.reso_prodotto(prodotti[nome], quantita)
            case '6':
                print("Arrivederci!")
                break
            case _:
                print("Opzione non valida. Riprova.")

# Esecuzione del menu della fabbrica
menu_fabbrica()
        
