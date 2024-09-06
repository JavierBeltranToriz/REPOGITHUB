#Operadores logicos and, or y not

import os
os.system("cls")

gas= False
encendido=True
edad=17

if gas and encendido:   
    print("puedes avanzar\n")
else:
    print("No puedes avanzar\n")

if gas or encendido:   
    print("puedes avanzar\n")
else:
    print("No puedes avanzar\n")
    
if not gas or encendido:
    print("Podemos avanzar")
else:
    print("No puedes avanzar")

if not gas or encendido or edad>17:
    print("Puedes avanzar")