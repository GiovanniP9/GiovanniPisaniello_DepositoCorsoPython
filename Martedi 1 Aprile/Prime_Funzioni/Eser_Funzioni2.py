#Funzione per generare sequenza di fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while True:
        numero_successivo = fib_sequence[-1] + fib_sequence[-2]
        if numero_successivo > n:
            break
        fib_sequence.append(numero_successivo)
    return fib_sequence

#funzione principale
def gioco():
    n = int(input("Quanti numeri Fibonacci vuoi generare? "))
    sequenza = fibonacci(n)
    print("La sequenza di Fibonacci generata è:", sequenza)
    
#Avvio del programma
gioco()