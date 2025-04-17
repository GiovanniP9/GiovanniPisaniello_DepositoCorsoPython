import numpy as np

def menu_array():
    print("MENU CREAZIONE ARRAY")
    print("inserisci valori:")
    while True:
        try:
            start = int(input("inserisci il valore di partenza: "))
            stop = int(input("inserisci il valore di arrivo: "))
            step = input("inserisci il passo: ")
        
            if start < 0 or stop < 0:
                print("I valori devono essere positivi")
                continue
        
            if step.strip() == "":
                step = 1
            else:
                step = int(step)
                if step <= 0:
                    print("Il passo deve essere positivo")
                    continue
        
            array = np.arange(start, stop, step)
            print("Array creato:", array)
            print("Tipo di dati:", array.dtype)
            return array
    
        except ValueError:
            print("Errore: inserire solo numeri interi validi.")
        except Exception as e:
            print(f"Si è verificato un errore: {e}")

def mostra_array_salvati(array_list):
    if not array_list:
        print("Nessun array salvato.")
        return
    
    print("Array salvati:")
    for i, arr in enumerate(array_list):
        print(f"Array {i+1}: {arr}")
        
def crea_matrice_da_array(array_list):
    if len(array_list) < 2:
        print("Non ci sono abbastanza array per creare una matrice.")
        return None
    
    lunghezze = [len(arr) for arr in array_list]
    if len(set(lunghezze)) != 1:
        print("Tutti gli array devono avere la stessa lunghezza per creare una matrice.")
        return None
    matrice = np.array(array_list)
    print("Matrice creata:\n", matrice)
    print("Forma della matrice:", matrice.shape)
    print("Tipo di dati della matrice:", matrice.dtype)

def menu():
    array_list = []
    while True:
        print("\nMENU PRINCIPALE")
        print("1. Crea un array")
        print("2. Mostra gli array salvati")
        print("3. Crea una matrice da array salvati")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            array = menu_array()
            array_list.append(array)
        elif scelta == "2":
            mostra_array_salvati(array_list)
        elif scelta == "3":
            crea_matrice_da_array(array_list)
        elif scelta == "4":
            break
        else:
            print("Opzione non valida, riprova.")

menu()
    

