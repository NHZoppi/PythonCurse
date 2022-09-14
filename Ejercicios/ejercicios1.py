#EJERCICIO 1
def mayor(number1, number2):
    if number1 > number2:
         return number1
    elif number2 > number1:
         return number2
    else:
        return "Son iguales"

print(mayor(2553,434))



#Ejercicio 2

def graterThree(num1, num2, num3):
     if num1 > num2 and num1 > num3:
         return num1
     elif num2 > num1 and num2 > num3:
         return num2
     elif num3 > num1 and num3 > num2:
         return num3

print(graterThree(8,9,7))

 # Ejercicio 3

def largoCadena(string):
    #Aca empezamos la cuenta desde 0
    cont = 0
    # Empezamos a contar los caracteres en el string
    for i in string:
        cont+= 1
    #retornamos cont con el contador  +=. IMPORTANTE Cuando bajamos el return tiene que estar a la altura del for!!!!!
    return cont

string = "Hola"
print(largoCadena(string))

# Ejercicio 4

def vocal(Voc):
    if Voc == "a" and "e" and "i" and "o" and "u":
        return True
    elif Voc == "A" and "E" and "I" and "O" and "U":
        return True
    else: return False
print (vocal("A"))

# Ejercicio 5

def sum1(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
print(sum1([1,23,4]))

def mult(lista):
    multi = 1
    for i in lista:
        multi *= i
    return multi
print(mult([2,3,4]))

# Ejercicio 6

def reverse(Str):
    cont = ""
    for i in Str:
        cont = i + cont
    return cont
print(reverse("Hola"))

# Mejor forma de hacer el ejercicio con un slice. Seleccionamos todo el string con :: y empezamos de atras para adelante, marcando e indice -1.
def reverse2(Str):
    print(Str[::-1])
reverse2("Carlos")

# Ejercicio 7

def es_polindromo(mismo):
    return mismo == reverse(mismo)
print(es_polindromo("paladar"))

# Ejercicio 8

def superposicion(lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False
print(superposicion(["tato", "cacho"], ["tato","tio"]))

# Ejercicio 9

def generar_n_caracteres(n, str):
    print(n * str)
generar_n_caracteres(5,"x")

# Ejercicio 10

def procedimiento(lista):
    for i in lista:
        print(i * "x")
procedimiento([1,2,3])