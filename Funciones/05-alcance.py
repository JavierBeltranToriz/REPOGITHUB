saludo="hola global"

def saludar():
    saludo=("Hola mundo")
    print(saludo)
    
def saludoJa():
    saludo=("Hola Javier")
    print(saludo)

def saludando():
    global saludo
    saludo=("Hola global función")
    print(saludo)

saludar()
saludoJa()
print(saludo)
saludando()