nome = 'Alice'
eta = 25
print("il mio nome è", nome, "e ho", eta, "anni.")

#INTERI
a= 5
b= -10
print(a, "e", b)
#FLOATING POINT NUMBERS
a= 5.6
b= -10.4
print(a, "e", b)

#STRING
a= "Ciao"
b= 'Mondo'
print(a, "e", b)

#ACCEDERE A UN CARATTERE DI UNA STRINGA
s = "Python"
print(s[0]) # P
print(s[1]) # y
print(s[2]) # t

#CONCATENAZIONE DI STRINGHE
saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio) # Ciao Alice

#print(s[100]) # Errore: string index out of range

# alcuni metodi delle stringhe
z= "ciao, mondo"
print(len(z)) # 10
print(z.upper()) # CIAO, MONDO
print(z.split(',')) # 'Ciao', ' mondo'
print(z.replace('ciao', 'Salve')) # Salve, mondo


 