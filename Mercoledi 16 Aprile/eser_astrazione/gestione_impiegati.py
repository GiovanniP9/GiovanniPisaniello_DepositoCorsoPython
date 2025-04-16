from abc import ABC, abstractmethod

class Impiegato(ABC): # Definizione della classe astratta
    def __init__(self, nome, cognome, stipendio):
        self.__nome = nome
        self.__cognome = cognome
        self.__stipendio = stipendio

    @abstractmethod # Metodo astratto da implementare nelle sottoclassi
    def calcola_stipendio(self):
        pass
    
    def get_nome(self):# Metodi getter per accedere ai dati privati
        return self.__nome
    
    def get_cognome(self):
        return self.__cognome
    
    def get_stipendio(self):
        return self.__stipendio
    
class Impiegato(Impiegato): # Definizione della classe concreta
    def __init__(self, nome, cognome, stipendio):
        super().__init__(nome, cognome, stipendio)
        
    def calcola_stipendio(self): # Metodo per calcolare lo stipendio
        # In questo caso, lo stipendio è fisso e non cambia
        return self.get_stipendio()
    
class ImpiegatoProvvigione(Impiegato):# Definizione della classe concreta
    def __init__(self, nome, cognome, stipendio, vendite, percentuale):
        super().__init__(nome, cognome, stipendio)
        self.__vendite = vendite
        self.__percentuale = percentuale
    def get_vendite(self):# Metodo getter per le vendite
        return self.__vendite
    def get_percentuale(self):# Metodo getter per la percentuale
        return self.__percentuale
    def calcola_stipendio(self):# Metodo per calcolare lo stipendio
        # Calcola lo stipendio base + bonus in base alle vendite
        bonus = self.get_vendite() * self.get_percentuale()
        return self.get_stipendio() + bonus

def inserisci_impiegato():# Funzione per inserire un nuovo impiegato
    print("Inserisci i dati dell'impiegato:")
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    stipendio = float(input("Stipendio: "))
    tipo = input("Tipo (1 per impiegato, 2 per impiegato a provvigione): ")
    # Verifica il tipo di impiegato
    if tipo == "1":
        impiegato = Impiegato(nome, cognome, stipendio)
    elif tipo == "2":
        vendite = float(input("Vendite: "))
        percentuale = float(input("Percentuale (es. 0.05 per 5%): "))
        impiegato = ImpiegatoProvvigione(nome, cognome, stipendio, vendite, percentuale)
    else:
        print("Tipo non valido.")
        return
    
#stampa gli impiegati
def stampa_impiegati(impiegati):
    if not impiegati:
        print("Nessun impiegato inserito.")
        return
    print("Lista degli impiegati:")
    for impiegato in impiegati:
        print(f"Nome: {impiegato.get_nome()}, Cognome: {impiegato.get_cognome()}, Stipendio: {impiegato.calcola_stipendio():.2f}")

def menu():# Funzione per il menu principale
    impiegati = []# Lista per memorizzare gli impiegati
    # Ciclo infinito per il menu
    while True:
        print("\n--- MENU ---")
        print("1. Inserisci un nuovo impiegato")
        print("2. Visualizza impiegati e stipendi")
        print("3. Esci")
        
        scelta = input("Scelta: ").strip()
        # Verifica la scelta dell'utente
        match scelta:
            case "1":# Inserisci un nuovo impiegato
                nuovo = inserisci_impiegato()
                if nuovo:
                    impiegati.append(nuovo)
                    print("Impiegato aggiunto con successo.")
            case "2":# Visualizza gli impiegati e i loro stipendi
                stampa_impiegati(impiegati)
            case "3":# Esci dal programma
                print("Uscita dal programma.")
                break
            case _:# Scelta non valida
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu()

