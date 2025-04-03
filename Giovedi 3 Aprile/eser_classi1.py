import math

class Punto:
    def __init__(self, x, y):# Costruttore del punto.
         self.x = x
         self.y = y
    def muovi(self, dx, dy): # Muove il punto di dx unità verso destra e dy unità verso l'alto.
         self.x += dx
         self.y += dy
    def distanza_da_origine(self):# Calcola la distanza dal punto all'origine.
        return math.sqrt(self.x**2 + self.y**2)# Restituisce la distanza.
    def __repr__(self): # Restituisce una stringa che rappresenta il punto.
        return f"Punto(x={self.x}, y={self.y})"

if __name__ == "__main__":
    x = int(input("Inserisci la coordinata x: "))
    y = int(input("Inserisci la coordinata y: "))
    P = Punto(x, y) # Creazione del punto P con coordinate (3, 4).
    print(f"Coordinate iniziali: ({P.x}, {P.y})")
    print(f"Distanza da origine: {P.distanza_da_origine()}")# Visualizza la distanza dal punto all'origine.
    dx = int(input("Inserisci la nuova coordinata x: "))
    dy = int(input("Inserisci la nuova coordinata y: "))
    P.muovi(dx, dy)# Muove il punto
    print(f"Coordinate post-movimento: ({P.x}, {P.y})")
    print(f"Distanza da origine dopo il movimento: {P.distanza_da_origine()}")# Visualizza la nuova distanza dal punto all'origine.

