import numpy as np
import mysql.connector

matrice =np.random.randint(1, 101, size=(6, 6)) # Crea una matrice 6x6 con valori casuali tra 1 e 100
print("Matrice originale:\n", matrice)
print("Tipo di dati:", matrice.dtype) # Output: int64

sottomatrice = matrice[1:5, 1:5] # Estrae una sottomatrice 4x4
print("Sottomatrice:\n", sottomatrice)

inverti_righe = matrice[::-1] # Inverte le righe della matrice
print("Matrice con righe invertite:\n", inverti_righe)

indici = np.arange(inverti_righe.shape[0]) # Crea un array di indici per la diagonale principale, shape[0] mi da la dimensione della matrice
diagonale = inverti_righe[indici, indici] # Estrae la diagonale principale usando gli indici
print("Diagonale principale:\n", diagonale)

modificata = inverti_righe.copy() # Crea una copia della matrice invertita
modificata[modificata % 3 == 0] = -1 # Modifica gli elementi divisibili per 3 con -1
print("Matrice modificata:\n", modificata)

# parte per inserire la matrice originale in un database

conn = mysql.connector.connect(
    host="localhost",        # Host del database (es. localhost)
    user="root",       # Il tuo nome utente MySQL
    password="GiFeTe251098?", # La tua password MySQL
    database="matrici"  # Nome del database a cui vuoi connetterti
)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS matrice (
    id INT AUTO_INCREMENT PRIMARY KEY,
    col1 INT, col2 INT, col3 INT, col4 INT, col5 INT, col6 INT
)
''')

for riga in matrice:
    dati = list(map(int, riga))
    cursor.execute('''
    INSERT INTO matrice (col1, col2, col3, col4, col5, col6)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', dati)

# Commit per salvare le modifiche
conn.commit()

# Seleziona e stampa i dati dalla tabella per vedere il contenuto
cursor.execute('SELECT * FROM matrice')

# Visualizza i dati nella tabella
print("Dati inseriti nel database:")
for riga in cursor.fetchall():
    print(riga)

# Chiudi la connessione al database
conn.close()