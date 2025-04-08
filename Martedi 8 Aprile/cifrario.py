
def cifra(testo,chiave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"# alfabeto minuscole
    risultato = ""
    
    for lettera in testo:
        if lettera.islower(): # cifra lettere minuscole
            posizione = alfabeto.find(lettera) # trova la posizione della lettera nel alfabeto
            nuova_posizione = (posizione + chiave) % 26 # calcola la nuova posizione con il modulo 26 che, permette di riportare la lettera al suo posto in modo ciclico
            risultato += alfabeto[nuova_posizione] #aggiunge la lettera alla risposta
        else:
            risultato += lettera # non cifra caratteri non alfabetici
    
    return risultato
def decifra(testo, chiave):# decifra una stringa
    return cifra(testo, -chiave)

def menu():
    while True:
        choise = int(input('Ciao! che operazione vuoi effettuare?  \n'
                           '1. Cifra una stringa \n'
                           '2. Decifra una stringa \n'
                           '3. Esci \n'))
        match choise:
            case 1:
                stringa = input('Inserisci la stringa da cifrare: ')
                chiave = int(input('Inserisci la chiave (0 - 25): '))
                testo_cifrato = cifra(stringa, chiave)
                print(testo_cifrato)
             

            case 2:
                stringa = input('Inserisci la stringa da cifrare: ')
                chiave = int(input('Inserisci la chiave (0 - 25): '))
                testo_cifrato = decifra(stringa, chiave)
                print(testo_cifrato)
                

            case 3:
                print('Cià')
                break
menu()