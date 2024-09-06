#Metodos de datos String
import os

os.system("cls")

animal="  ChanCHito Feliz   "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal.strip())
print(animal.strip().capitalize())
print(animal.strip().rstrip().capitalize())
print(animal.find("CH"))
print(animal.find("cH"))
print(animal.upper().find("CH"))
print(animal.replace("CH","j"))
print("CH" in animal)
print("CH" not in animal)