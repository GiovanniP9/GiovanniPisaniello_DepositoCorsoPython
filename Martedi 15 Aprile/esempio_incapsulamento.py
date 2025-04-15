class Computer:
    def __init__(self):
        self.__processore = "Intel i5" # Attributo privato

    def get_processore(self):
        return self.__processore # __processore è chiamato in modo privato con il __ 

    def set_processore(self, processore):
        self.__processore = processore

pc = Computer()
# Accede all'attributo privato tramite il getter
print(pc.get_processore()) #non serve per forza usare prima il getter e poi il setter
# Modifica l'attributo privato tramite il setter
pc.set_processore("AMD Ryzen 5")
print(pc.get_processore())# usa IL GETTER per visualizzare la modifica

# Variabile globale
numero = 10

def funzione_esterna():
 # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)
    def funzione_interna():
    # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)
    funzione_interna()

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)
