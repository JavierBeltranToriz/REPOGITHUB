import os
os.system("cls")

print("Bienvenido a la calculadora")
print("para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado=""
while True:
    if not resultado:
        resultado=input("Ingrese N1: ")
        if resultado.lower()=="salir":
            break
        resultado=int(resultado)
    op=input("Ingresa la operación: ")
    if op.lower()=="salir":
        break
    n2=input("Ingresa N2: ")
    #op=input("Ingresa la operación: ")
    if n2.lower()=="salir":
        break
    
    n2=int(n2)
    if op.lower()=="suma":
        resultado +=n2
    elif op.lower()=="resta":
        resultado -=n2
    elif op.lower()=="multi":
        resultado *=n2
    elif op.lower()=="div":
        resultado /=n2
    else:
        print("Operación no valida")
        break       
      
    print(f"El resultado es :{resultado}")
    