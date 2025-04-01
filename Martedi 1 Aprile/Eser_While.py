# Esercizio 1: Scrivere un programma che calcoli la somma di una serie di numeri interi inseriti dall'utente. Il programma deve terminare quando l'utente inserisce il numero 0.
# Inizializza la somma a zero
somma = 0
while True: # Inizio del ciclo infinito
    # Chiede all'utente di inserire un numero
    n = int(input("Inserisci un numero (0 per terminare): "))
    if n == 0: # Se l'utente inserisce 0, esci dal ciclo
        print("Hai inserito 0, il programma termina.")
        break
    somma += n
print("La somma dei numeri inseriti è:", somma)