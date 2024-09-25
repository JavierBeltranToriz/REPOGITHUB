def cls(nombre, apellido="Toriz"):
    import os
    os.system("cls")
    print("Hola Mundo")
    print("Ultimate Python")
    
    print(f"Hola {nombre} {apellido}, Bienvenido")


nom=input("Cual es tu nombre:")
ape=input("Cual es tu apellido:")
cls(nom,ape)
cls(apellido="Toriz",nombre="Javier")


