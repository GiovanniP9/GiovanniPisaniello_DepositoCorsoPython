import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GiFeTe251098?",
  database="corsopython"
)
mydb.close() # chiudo la connessione alla database

mycursor = mydb.cursor() # creazione del cursore per eseguire le query
# query = "CREATE TABLE utenti(ID INT PRIMARY KEY, NOME VARCHAR(50), INDIRIZZO VARCHAR(50))"
# # query = "CREATE DATABASE corsopython"
# query = "SHOW DATABASES" # creo una query per visualizzare tutte le database
# query = "SHOW TABLES"
def insertManyRow(dati):
  query = "INSERT INTO utenti (NOME, INDIRIZZO) VALUES (%s, %s)" # creo una query per inserire un record di utenti e %s e %s sono placeholder per i valori da inserire
  # val = [("Tommaso", "Via San Marco"),("Maria", "Via Napoli")] # valori da inserire
  # query = "ALTER TABLE utenti MODIFY ID INT AUTO_INCREMENT" # creo una query per aggiungere una colonna alla tabella utenti
  # mycursor.execute(query) # eseguo la query
  mycursor.executemany(query,dati) # eseguo la query

  mydb.commit() # committo le modifiche

  print(mycursor.rowcount, "righe inserite.")
  print(mycursor.lastrowid, "ultimo ID inserito.")

def readRows(): # creo una query per visualizzare tutti i record di utenti
  query = "SELECT * FROM utenti"
  mycursor.execute(query)
  result = mycursor.fetchall() # recupero tutti i record
  for row in result:
    print(row)
readRows()

def readRow(): # creo una query per visualizzare tutti i record di utenti
  query = "SELECT * FROM utenti"
  mycursor.execute(query)
  result = mycursor.fetchone() # recupero tutti i record
  print(result)

readRow()