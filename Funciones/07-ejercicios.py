# Palindromo
import os
os.system("cls")

       
def nospace(texto):
    nuevo_texto=""
    for char in texto:
        if char!=" ":
            nuevo_texto +=char
    return nuevo_texto    

def invertir(texto):
    nuevo_texto=""
    for char in texto:
        if char!=" ":
            nuevo_texto =char + nuevo_texto
    return nuevo_texto   
    
def es_palindromo(texto):
    texto=nospace(texto)
    print(texto)
    texto2=invertir(texto)
    print(texto2)
    
    return texto.lower() ==texto2.lower()  

print("amo la paloma: ", es_palindromo("somos o no somos"))