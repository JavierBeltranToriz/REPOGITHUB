#Sentencia de comparación

import os
os.system("cls")

for num in range(5):
    print(num+1, num * 'Hola mundo ')
    
buscar=7

for num in range(5):
    print (num)
    if num == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado :(")

