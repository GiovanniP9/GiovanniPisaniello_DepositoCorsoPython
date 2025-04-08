import random

def  range_numeri(): # genera un range di numeri casuali
    while True:
        try:
            mini = int(input("Inserisci il numero minimo: "))
            maxi = int(input("Inserisci il numero massimo: "))
            if mini < maxi: # controllo se il range e' valido
                return mini, maxi
            else:
                print("Il numero minimo non può essere maggiore del numero massimo.")
        except ValueError:
            print("Devi inserire un numero valido.")

def scrivi_file(nome_file,mini, maxi):
    numeri = random.sample(range(mini, maxi+1), 5) # genera 5 numeri casuali tra 
    with open(nome_file, 'w') as file:
        file.write(' '.join(map(str, numeri))) # scrive i numeri separati da spazio

def leggi_file(nome_file):
    with open(nome_file, 'r') as file:
        contenuto = file.read()
        return list(map(int, contenuto.split())) # converte la stringa in una lista di numeri

def indovina_numero(mini, maxi):
    tentativi = []
    while len(tentativi) < 2:
        try:
            numero = int(input(f"Indovina il numero, tentativo {len(tentativi) + 1} (tra {mini} e {maxi}): "))
            if mini <= numero <= maxi: # controllo se il numero e' compreso tra
                tentativi.append(numero)
            else:
                print("Il numero non e' valido. Inserisci un numero tra 1 e 50.")
        except ValueError:
            print("Devi inserire un numero valido.")
    return tentativi

def gioca():
    nome_file = "numeri.txt" # nome del file in cui salvare i numeri casuali
    mini, maxi = range_numeri()
    scrivi_file(nome_file,mini, maxi) # salva i numeri casuali nel file
    numeri_gioco = leggi_file(nome_file) # legge i numeri casuali dal file
    print("ho scritto 5 numeri casuali. Indovina almeno due")
    tentativi = indovina_numero(mini, maxi) # indovina i numeri
    indovinati = [n for n in tentativi if n in numeri_gioco] # numeri indovinati
    
    print(f"numeri nel file: {numeri_gioco}")
    print(f" numeri indovinati: {indovinati}")
    print(f"Hai indovinato {len(indovinati)} numeri.")

gioca()
