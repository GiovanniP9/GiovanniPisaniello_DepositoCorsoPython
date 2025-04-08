
def calcola_media(voti):
    return sum(voti) / len(voti)

def leggi_file(nome_file):
    dizionario = {}
    try:
        with open(nome_file, 'r') as file:
            file.readline()
    except FileNotFoundError:
        print(f"Il file '{nome_file}' non esiste.")
        pass
    return dizionario

def scrivi_file(nome_file, dizionario):
    with open(nome_file, 'w') as file:
        file.writelines()  # scrivi intestazione file
        
            
def aggiungi_alunno(dizionario):
    nome = input("Insertisci il nome dell'alunno: ")
    if nome in dizionario:
        print("L'alunno già esiste.")
        return
    voti = []
    print("Inserisci i voti dell'alunno (scrivi fine per terminare): ")
    while True:
        voto = input("Inserisci un voto: ")
        if voto.lower() == "fine":
            break
        try:
            voti.append(float(voto))
        except ValueError:
            print("Il voto deve essere un numero.")
    
    if not voti:
        print("Devi inserire almeno un voto.")
        return
    
    media = calcola_media(voti)
    dizionario[nome] = {
        "voti": voti,
        "media": media}
    scrivi_file("classe.txt", dizionario)
    print(f"Alunno '{nome}' aggiunto con media {media}.")
    
def mostra_alunni(dizionario):
    if not dizionario:
        print("Nessun alunno presente.")
        return
    
    print("Alunni e medie:")
    for nome, info in dizionario.items():
        voti_str = ', '.join(map(str, info['voti']))
        print(f"{nome}: voti = {voti_str}, media = {info['media']:.2f}")

def menu():
    dizionario = leggi_file("classe.txt")
    while True:
        print("\n1. Aggiungi alunno")
        print("2. Mostra alunni")
        print("3. Esci")
        scelta = int(input("Scelta: "))
        
        match scelta:
            case 1: 
                aggiungi_alunno(dizionario)
            case 2: 
                mostra_alunni(dizionario)
            case 3:
                print("Uscita dal programma.")
                break
menu()