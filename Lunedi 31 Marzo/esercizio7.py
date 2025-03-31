#esercizio 7
while True:

  print("Inserisci numero per conto alla rovescia")
  num = int(input())
  #ciclo di conto alla rovescia
  for i in range(num, -1, -1):
      print(i)
  print("Fine conto alla rovescia")
  
  #ciclo di controllo per ripetere il conto alla rovescia
  print("Vuoi ripetere? (s/n): ")
  risposta = input()
  if risposta == "n":
        break

  
