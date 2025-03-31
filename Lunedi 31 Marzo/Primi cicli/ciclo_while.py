#ciclo matematico
conteggio = 0
while conteggio < 10:
    print(conteggio)
    conteggio += 1
print("Fine ciclo while")

#ciclo booleano
controllo = True
while controllo:
    print("Ciclo infinito")
    risposta = input("Vuoi continuare? (s/n): ")
    if risposta == "n":
        controllo = False
print("Fine ciclo while")

