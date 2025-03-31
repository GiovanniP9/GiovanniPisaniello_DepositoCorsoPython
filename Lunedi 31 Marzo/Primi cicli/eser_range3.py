

while True:
    scelta = input("Vuoi inserire numeri o stringhe? (n/s): ")
    if scelta.lower() == 'n':
        numero1 = int(input("Inserisci il primo numero: "))
        numero2 = int(input("Inserisci il secondo numero: "))
        
        fattori_comuni = []# lista per memorizzare i fattori comuni
        # ciclo per trovare i fattori comuni
        for i in range(1, min(numero1, numero2) + 1):
            if numero1 % i == 0 and numero2 % i == 0:
                fattori_comuni.append(i)
        if len(fattori_comuni) == 0: # se non ci sono fattori comuni
            print("Non ci sono fattori comuni")
        else: # se ci sono fattori comuni
            print("Il massimo comune divisore e':", max(fattori_comuni))
        
    elif scelta.lower() == 's': # se l'utente vuole inserire stringhe
        stringa1 = input("Inserisci la prima stringa: ")
        stringa2 = input("Inserisci la seconda stringa: ")
        stringa1.sort() # ordino le stringhe
        stringa2.sort()# ordino le stringhe
        #controllo se le stringhe sono acronimi
        if stringa1 == stringa2:
            print("Le stringhe sono degli acronimi")
        else:
            print("Le stringhe non sono acronimi")
        

        