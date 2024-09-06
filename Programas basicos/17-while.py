import os
os.system("cls")

nume=1

while nume<100:
    print(nume)
    nume*=2
    
comando=""

while comando.lower() != "salir":
    comando=input("$ ")
    print(comando)