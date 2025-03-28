# esercizio 2
# scrivi un programma che permetta di gestire una lista di stringhe.
# Il programma deve consentire di:
# aggiungere una stringa alla lista
# rimuovere una stringa dalla lista
# visualizzare la lista
# eliminare la lista
# aggiungere una stringa in una posizione specifica
# rimuovere una stringa in una posizione specifica

lista = []
while True: # Inizio del ciclo infinito
      print("1, aggiungi stringa")
      print("2, rimuovi stringa")
      print("3, visualizza lista")
      print("4, elimina lista")
      print("5, aggiungi stringa in posizione")
      print("6, rimuovi stringa in posizione")
      print("0, esci")

      #input stringa
      scelta = input("Scegli un'opzione (1-6): ")
      
        #controllo input
      if scelta == "1": # Aggiungi stringa
       stringa = input("Inserisci una stringa: ")
       lista.append(stringa)
       print("Stringa aggiunta alla lista.")
      elif scelta == "2": # Rimuovi stringa
       stringa = input("Inserisci la stringa da rimuovere: ")
       lista.remove(stringa)
       print("Stringa rimossa dalla lista.")
      elif scelta == "3": # Visualizza lista
       print("Lista:", lista)
      elif scelta == "4": # Elimina lista
       lista.clear()
       print("Lista eliminata.")
      elif scelta == "5": # Aggiungi stringa in posizione
       stringa = input("Inserisci una stringa: ") # Chiede all'utente di inserire una stringa
       posizione = int(input("Inserisci la posizione in cui aggiungere la stringa: ")) # Chiede all'utente di inserire la posizione
       lista.insert(posizione, stringa)
       print("Stringa aggiunta alla posizione", posizione, "nella lista.")
      elif scelta == "6": # Rimuovi stringa in posizione
       posizione = int(input("Inserisci la posizione della stringa da rimuovere: "))
       lista.pop(posizione)
       print("Stringa rimossa dalla posizione", posizione, "nella lista.")
      elif scelta == "0": # Esci
         print("Uscita dal programma.")
         break
      else: # Opzione non valida
            print("Opzione non valida. Riprova.")
    