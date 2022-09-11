# Desde ahora las funciones que vimos son: 
# Print() Imprime en pantalla la estructura
# dir() Muestra los comandos para diferentes tipos de datos
# type() Nos da informacion de que tipo son
# UNA FUNCION ES UN BLOQUE DE CÓDIGO QUE REALIZA ALGUNA OPERACIÓN. Una función puede definir opcionalmente parámetros de entrada que permiten a los llamadores pasar argumentos a la función. Una función también puede devolver un valor como salida.

# Siempre pone DEF antes de comenzar una funcion, ya que con esta la definimos.

def hello(name = "person"):
    print ("HELLO " + name)
# Siempre hay que llamar a la funcion donde se quiera que se active. Sino esta no funcionara
hello ("joe")
hello ("Juan")
hello ("Carlos")



def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(23,232))
print(add(2323,4352))


add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10,30))