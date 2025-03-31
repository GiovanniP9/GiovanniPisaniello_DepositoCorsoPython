
while True:
    
    primo_intervallo = int(input("Inserisci il primo numero dell'intervallo: "))
    secondo_intervallo = int(input("Inserisci il secondo numero dell'intervallo: "))
    
    if primo_intervallo > secondo_intervallo:
        primo_intervallo, secondo_intervallo = secondo_intervallo, primo_intervallo #scambio i valori
    numeri_primi = []
    numeri_non_primi = []
    #ciclo per inserire i numeri nell'intervallo
    for num in range(primo_intervallo, secondo_intervallo + 1):# uso range(primo_intervallo, secondo_intervallo + 1) per includere il secondo numero
        if num > 1:
            primo = True #inizializzo la variabile primo a True
            for i in range(2, int(num**0.5)+1): #controllo fino alla radice quadrata del numero
                if num % i == 0: #controllo se il numero e' divisibile per i è uguale a 0
                    primo = False #se il numero e' divisibile per i
                    break
            if primo: #se il numero e' primo
                numeri_primi.append(num)
            else: #se il numero non e' primo
                numeri_non_primi.append(num)    
        else:
            numeri_non_primi.append(num)   
    #stampo i numeri primi e non primi
    print("I numeri primi nell'intervallo sono:", numeri_primi)
    print("I numeri non primi nell'intervallo sono:", numeri_non_primi)
    risposta = input("Vuoi continuare? (s/n): ")
    if risposta == "n":
        break
    