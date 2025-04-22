import mysql.connector
from mysql.connector import Error
import numpy as np

#funzione creazione database e tabella
def create_database_and_table(nome_db):
    try:
        # Connessione al server MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='GiFeTe251098?',# 'password' del tuo server MySQL
        )
        cursor = conn.cursor()
        # Creazione del database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_db}")
        # Selezione del database
        cursor.execute(f"USE {nome_db}")
        # Creazione della tabella
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prodotti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                categoria VARCHAR(255) NOT NULL,
                prezzo FLOAT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clienti (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendite (
                id INT AUTO_INCREMENT PRIMARY KEY,
                prodotto_id INT NOT NULL,
                cliente_id INT NOT NULL,
                quantita INT NOT NULL,
                data DATE NOT NULL,
                FOREIGN KEY (prodotto_id) REFERENCES prodotti(id),
                FOREIGN KEY (cliente_id) REFERENCES clienti(id)
            )
        """)
        
        prodotti = [
            ('Prodotto A', 'Categoria 1', 10.99),
            ('Prodotto B', 'Categoria 2', 20.50),
            ('Prodotto C', 'Categoria 1', 15.75),
            ('Prodotto D', 'Categoria 3', 30.00),
            ('Prodotto E', 'Categoria 2', 25.00)
        ]
        clienti = [
            ('Mario Rossi', 'mario.rossi@example.com'),
            ('Giulia Bianchi', 'giulia.bianchi@example.com'),
            ('Marco Verdi', 'marco.verdi@example.com')
        ]
        vendite = [
            (1, 1, 2, '2023-01-01'),# Prodotto A venduto a Mario Rossi in quantità 2 il 2023-01-01
            (2, 2, 1, '2023-01-02'),# Prodotto B venduto a Giulia Bianchi in quantità 1 il 2023-01-02
            (3, 3, 3, '2023-01-03'),# Prodotto C venduto a Marco Verdi in quantità 3 il 2023-01-03
            (4, 2, 2, '2023-01-04'),# Prodotto D venduto a Giulia Bianchi in quantità 2 il 2023-01-04
            (5, 1, 1, '2023-01-05') # Prodotto E venduto a Mario Rossi in quantità 1 il 2023-01-05
        ]
        # Inserimento dei dati nella tabella prodotti
        cursor.executemany("INSERT INTO prodotti (nome, categoria, prezzo) VALUES (%s, %s, %s)", prodotti)
        # Inserimento dei dati nella tabella clienti
        cursor.executemany("INSERT INTO clienti (nome, email) VALUES (%s, %s)", clienti)
        # Inserimento dei dati nella tabella vendite
        cursor.executemany("INSERT INTO vendite (prodotto_id, cliente_id, quantita, data) VALUES (%s, %s, %s, %s)", vendite)
        # Commit delle modifiche
        conn.commit()
        print("Database e tabelle creati con successo!")
    except Error as e:
        print(f"Errore durante la creazione del database: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

#funzione per connettersi al database
def connect_to_database(nome_db):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='GiFeTe251098?',# 'password' del tuo server MySQL
            database=nome_db
        )
        if conn.is_connected():
            return conn
    except Error as e:
        if "Unknown database" in str(e):# Errore di database sconosciuto
            # Se il database non esiste, crealo
            print(f"Database {nome_db} non trovato. Creazione del database...")
            #richiamo la creazione del database e della tabella
            create_database_and_table(nome_db)
            return connect_to_database(nome_db)
        else:
            print(f"Errore durante la connessione al database: {e}")
            return None

#funzione per calcolare la media dei prezzi con NumPy
def media_prezzi(conn):
    try:
        cursor = conn.cursor()
        # Esegui la query per calcolare la media dei prezzi
        cursor.execute("SELECT prezzo FROM prodotti")
        dati = cursor.fetchall()
        prezzi = np.array(dati, dtype=float).flatten()  # Converti i dati in un array NumPy
        # Calcola la media dei prezzi
        media = np.mean(prezzi)
        print(f"La media dei prezzi è: {media}")
    except Error as e:
        print(f"Errore durante il calcolo della media dei prezzi: {e}")
        
#definisco la funzione per calcolare la quantità media venduta con NumPy
def quantita_media_vendite(conn):
    try:
        cursor = conn.cursor()
        # Esegui la query per calcolare la quantità media venduta
        cursor.execute("SELECT quantita FROM vendite")
        dati = cursor.fetchall()
        quantita = np.array(dati, dtype=int).flatten()  # Converti i dati in un array NumPy
        # Calcola la quantità media venduta
        quantita_media = np.mean(quantita)
        print(f"La quantità media venduta è: {quantita_media}")
    except Error as e:
        print(f"Errore durante il calcolo della quantità media venduta: {e}")
        
#definisco la funzione per calcolare le vendite per categoria con NumPy
def vendite_per_categoria(conn):
    try:
        cursor=conn.cursor()
        cursor.execute("""
            SELECT p.categoria, v.quantita * p.prezzo AS totale_vendite
            FROM vendite v
            JOIN prodotti p ON v.prodotto_id = p.id
        """)
        dati = cursor.fetchall()
        if not dati:
            print("Nessuna vendita trovata.")
            return
        
        # Converti i dati in un array NumPy
        categorie = np.array([d[0] for d in dati])
        vendite = np.array([d[1] for d in dati], dtype=float)
        # Calcola le vendite totali per categoria
        uniche = np.unique(categorie) # crea un array di categorie uniche
        print("Vendite per categoria:")
        for categoria in uniche:
            totale_categoria = np.sum(vendite[categorie == categoria]) # Calcola il totale delle vendite per ogni categoria usando NumPy
            # Stampa il totale delle vendite per ogni categoria
            print(f"{categoria}: {totale_categoria}")
    except Error as e:
        print(f"Errore durante il calcolo delle vendite per categoria: {e}")

def prodotto_con_piu_vendite(conn):
    try:
        cursor = conn.cursor()
        # Esegui la query per calcolare il prodotto con più vendite
        cursor.execute("SELECT prodotto_id, quantita FROM vendite")
        dati = cursor.fetchall()
        if not dati:
            print("Nessuna vendita trovata.")
            return
        # Converti i dati in un array NumPy
        vendite = np.array(dati, dtype='int64')
        # Calcola il prodotto con più vendite
        prodotti, quantita = vendite[:, 0], vendite[:, 1] # Estrai gli ID dei prodotti e le quantità vendute
        unici = np.unique(prodotti) # crea un array di prodotti unici
        totali= np.array([quantita[prodotti == p].sum() for p in unici]) # Calcola il totale delle vendite per ogni prodotto usando NumPy
        indice_max = np.argmax(totali) # Trova l'indice del prodotto con più vendite
        prodotto_piu_venduto = unici[indice_max] # Trova il prodotto con più vendite
        
        cursor.execute("SELECT nome FROM prodotti WHERE id = %s", (int(prodotto_piu_venduto),))
        nome_prodotto = cursor.fetchone()[0] # Ottieni il nome del prodotto
        print(f"Il prodotto con più vendite è: {nome_prodotto} con {totali[indice_max]} vendite.")
    except Error as e:
        print(f"Errore durante il calcolo del prodotto con più vendite: {e}")
    
def menu(conn):
    while True:
        print("\nMENU ANALISI DATI CON NUMPY")
        print("1. Calcola media dei prezzi dei prodotti")
        print("2. Calcola quantità media venduta")
        print("3. Mostra vendite totali per categoria")
        print("4. Prodotto con più vendite")
        print("0. Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                media_prezzi(conn)
            case "2":
                quantita_media_vendite(conn)
            case "3":
                vendite_per_categoria(conn)
            case "4":
                prodotto_con_piu_vendite(conn)
            case "0":
                print("Uscita dal programma.")
                break
            case _:
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    nome_db = input("Inserisci il nome del database: ")
    conn = connect_to_database(nome_db)
    if conn:
        print("Connessione al database avvenuta con successo!")
        menu(conn)
        conn.close()
    else:
        print("Impossibile connettersi al database.")