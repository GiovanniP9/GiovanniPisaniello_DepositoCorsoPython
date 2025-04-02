from riassunti import *

# Creazione di un menu per richiamare singoli argomenti studiati

comando = True

while True:
    print("Menu:")
    print("1. Python")
    print("2. UML")
    print("3. Print()")
    print("4. Input()")
    print("5. Tipo di dato")
    print("6. Operatori logici + IF-ELIF-ELSE")
    print("7. Liste")
    print("8. Match")
    print("9. While e range()")
    print("10. funzioni")
    print("11. chiudi")
    
    scelta = int(input("Scegli un argomento (1-11): "))
    match scelta:
        case 1: # richiamo la funzione che elenca gli argomenti di Python
            cosa_e_python()
        case 2: #richiamo la funzione che elenca gli argomenti di UML
            uml()
        case 3: #richiamo la funzione che elenca gli argomenti di print()
            uso_di_print()
        case 4: #richiamo la funzione che elenca gli argomenti di input()
            uso_di_input()
        case 5: #richiamo la funzione che elenca gli argomenti di tipo di dato
            tipi_di_dato()
        case 6: #richiamo la funzione che elenca gli argomenti degli operatori logici + IF-ELIF-ELSE
            operatore_logici_e_strutture_di_controllo()
        case 7: #richiamo la funzione che elenca gli argomenti delle liste
            liste()
        case 8: #richiamo la funzione che elenca gli argomenti del match
            match_case()
        case 9: #richiamo la funzione che elenca gli argomenti del while e range()
            uso_di_while_e_range()
        case 10: #richiamo la funzione che elenca gli argomenti delle funzioni
            somma(3, 5)
        case 11: # usciamo dal programma
            print("Arrivederci!")
            comando = False
            break
            
            
    