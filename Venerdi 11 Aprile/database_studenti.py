import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GiFeTe251098?",
  database="classestudenti"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE IF NOT EXISTS classestudenti")

def crea_tabella_studenti():
    query = """ CREATE TABLE IF NOT EXISTS STUDENTI (
        MATRICOLA INT AUTO_INCREMENT PRIMARY KEY,
        NOME VARCHAR(50) NOT NULL,
        COGNOME VARCHAR(50) NOT NULL
        
    )"""	
    mycursor.execute(query)
    mycursor.execute("ALTER TABLE STUDENTI AUTO_INCREMENT = 1000")
    print("Tabella STUDENTI pronta.")

def aggiungi_studente(my_cursor, table):
    nome = input('\nInserisci il nome dell\'alunno: ').strip()
    cognome = input('\nInserisci il cognome dell\'alunno: ').strip()
    
    query = f'INSERT INTO {table} (NOME, COGNOME) VALUES(%s,%s)'
    values = (nome.upper(), cognome.upper())
    my_cursor.execute(query, values)
    mydb.commit()
    print(f"{nome.upper()} {cognome.upper()} aggiunto.")
    
def elimina_studente(my_cursor, table):
    while True:
        nome = input('\nInserisci il nome dell\'alunno: ').strip()
        cognome = input('\nInserisci il cognome dell\'alunno: ').strip()
        values = (nome.upper(), cognome.upper())
        query = f'SELECT * FROM {table} WHERE NOME = %s AND COGNOME = %s'
        my_cursor.execute(query, values)
        res = my_cursor.fetchone()
        print(res)
    
        if res:
            conferma = int(input('Vuoi eliminare questo alunno? (1/Sì, 2/No)'))
            if conferma == 1:
                query = f'DELETE FROM {table} WHERE NOME = %s AND COGNOME = %s'
                my_cursor.execute(query, values)
                mydb.commit()
                print(f'{nome}, {cognome} eliminato.')
                break
            elif conferma == 2:
                print('Ripeti operazione')
                continue
            else:
                print('Errore, opzione non valida')
                continue
        else:
            print(f"Studente {nome} {cognome} non trovato.")

def menu():
    crea_tabella_studenti()
    while True:
         print("\n=== MENU STUDENTI ===")
         print("1. Aggiungi studente")
         print("2. Elimina studente")
         print("3. Esci")

         scelta = input("Scegli un'opzione (1-3): ")

         match scelta:
            case "1":
                aggiungi_studente(mycursor, "STUDENTI")
            case "2":
                elimina_studente(mycursor, "STUDENTI")
            case "3":
                print("Uscita dal programma.")
                break
            case _:
                print("Scelta non valida. Riprova.")

    mycursor.close()
    mydb.close()

menu()