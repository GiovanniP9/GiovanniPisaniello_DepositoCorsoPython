def è_palindroma(stringa):
    nuova_stringa = ''.join(filter(str.isalpha, stringa))    #rimuovere tutto tranne le lettere alfabetiche
    return nuova_stringa == nuova_stringa[::-1]  # controlla se la stringa è palindroma confrontando la stringa con la sua inversa e ritorna il risultato
def risultato_palindroma(frase):
    if è_palindroma(frase): # verifica se la frase è palindroma
        return "La frase è palindroma"
    else: # se la frase non è palindroma
        return "La frase non è palindroma"
frase = input ("Inserisci una frase: ").lower()  # trasforma la frase in minuscolo per evitare differenze di lettere maiuscole e minuscole
print(risultato_palindroma(frase))

# def è_palindroma(stringa):
#     return ''.join(filter(str.isalpha, stringa.lower())) == ''.join(filter(str.isalpha, stringa.lower()))[::-1]
# def mostra_risultato(stringa):
#     return "È palindroma!" if è_palindroma(stringa) else "Non è palindroma."
# print(mostra_risultato(input("Inserisci una parola o frase: ")))