from collections import Counter

def duplicati_parole(stringa):
    parole = [word.lower() for word in stringa.split() if word.isalnum()] # Divide la stringa in parole, rimuovendo caratteri speciali e convertendo tutto in minuscolo
    contatore = Counter(parole) # Crea un Counter a partire dalle parole
    duplicati = {parola: count for parola, count in contatore.items() if count > 1} # Crea un dizionario con le parole duplicate e i rispettivi contatori
    #mostra i caratteri duplicati
    if duplicati:
        print("Parole duplicate:")
        for parola, count in duplicati.items(): # Stampa le parole duplicate
            print(f"{parola}: {len(parola)} caratteri, ripetuta {count} volte") # Stampa la parola, la lunghezza e il numero di ripetizioni
        
    else:
        print("Nessuna parola duplicata presente.")

stringa = input("Inserisci una stringa: ").lower() # Converte la stringa in minuscolo per facilitare il controllo delle parole duplicate

duplicati_parole(stringa) # Chiamata alla funzione per controllare le parole duplicate

# def duplicato(stringa):
#     stringa = ''.join(i for i in stringa if i.isalnum()) # Elimina caratteri non alfanumerici
#     conteggio = Counter(stringa) # Crea un oggetto Counter a partire dalla stringa
#     duplicati = {char: count for char, count in conteggio.items() if count > 1} # Crea un dizionario con i caratteri duplicati
#     lunghezza_duplicati = sum(count * len(char) for char, count in duplicati.items()) # Calcola la lunghezza dei caratteri duplicati
#     if duplicati:
#         print("Caratteri duplicati:")
#         for char, count in duplicati.items():
#             print(f"{char}: {count} volta(e)")
#         print(f"La lunghezza dei caratteri duplicati è {lunghezza_duplicati} caratteri.")
#     else:
#         print("Nessun carattere duplicato presente.")


# stringa = input("Inserisci una stringa: ").lower()

# duplicato(stringa)





