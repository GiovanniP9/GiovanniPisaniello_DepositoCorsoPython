
#funzione per calcolare la media dei voti
def calcola_media(voti):
    return sum(voti) / len(voti) # Calcola la media dei voti

# funzione per aggiungere un alunno e i suoi voti
def aggiungi_alunno(dizionario):
    nome = input("Inserisci il nome dell'alunno: ")
    voti = []
    print("Inserisci i voti dell'alunno separati da uno spazio: ")
    while True:
        voto = input()
        if voto.lower() == "fine":
            break
        voti.append(voto) # Aggiungi il voto alla lista dei voti
    voti = [float(voto) for voto in voti]  # Converti i voti in float
    media = calcola_media(voti) # Calcola la media dei voti
    dizionario[nome] = { # Aggiungi l'alunno al dizionario
        "voti": voti,  # Aggiungi i voti all'alunno
        "media": media } # Aggiungi la media all'alunno   
    print(f"Alunno {nome} aggiunto con media {media:.2f}.")
    
def mostra_media(dizionario):# Mostra la media di tutti gli alunni
    if dizionario: # Se il dizionario non è vuoto
        for nome, dati in dizionario.items(): # Itera su ogni alunno e i suoi dati
            print(f"{nome}: voti = {dati['voti']}, media = {dati['media']}") #stampa il nome dell'alunno, i voti e la media
    else:
        print("Nessun alunno presente.")

def menu():
    dizionario = {} # Inizializza un dizionario vuoto per memorizzare gli alunni e le loro medie
    while True:
        print("1. Aggiungi alunno")
        print("2. Mostra media alunni")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")
        
        match scelta:
            case '1': # Aggiungi un alunno
                aggiungi_alunno(dizionario)
            case '2': # Mostra la media di tutti gli alunni
                mostra_media(dizionario)
            case '3': # Esci dal programma
                print("Uscita dal programma.")
                break        
menu()