#Creando la primera app

import os
os.system("cls")

n1=input("Ingresa el primer Numero: ")
n2=input("Ingresa el segundo Numero: ")

print(n1, " ",n2)
print(n1 + n2)

n1=int(n1)
n2=int(n2)
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2)
print(n1 % n2)

suma=n1+n2
resta=n1-n2
multi=n1*n2
div=n1/n2

mensaje=f"""
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicación es {multi}
el resultado de la división es {div}.
"""

print(mensaje)