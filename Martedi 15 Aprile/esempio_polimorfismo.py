# class Animale:
#     def emetti_suono(self):
#         print("Questo animale fa un suono")

# class Cane(Animale):
#     def emetti_suono(self):
#         print("Bau")

# class Gatto(Animale):
#     def emetti_suono(self):
#         print("Miao")

# def fai_parlare(animale):
#     print(animale.emetti_suono())

# cane = Cane()
# gatto = Gatto()

# fai_parlare(gatto)
# fai_parlare(cane) 

class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")
        
class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")
        
def disegna_figura(figura):
    # Anche qui, basta che 'figura' abbia il metodo 'disegna'
    figura.disegna()
    
figure = [Cerchio(), Rettangolo()] # figure[0]=Cerchio() / figure[1]=Rettagolo()

# Iteriamo e disegniamo ogni figura
for figura in figure:
    disegna_figura(figura)