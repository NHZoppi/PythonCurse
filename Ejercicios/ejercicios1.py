#EJERCICIO 1

# def mayor(number1, number2):
#     if number1 > number2:
#         return number1
#     else: 
#         return number2
# print(mayor(2553,124))

#Ejercicio 2

# def graterThree(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     elif num3 > num1 and num3 > num2:
#         return num3 

# print(graterThree(8,9,7))

def largoCadena(string):
    #Aca empezamos la cuenta desde 0
    cont = 0
    # Empezamos a contar los caracteres en el string
    for i in string:
        cont+= 1
    #retornamos cont con el contador  +=. IMPORTANTE Cuando bajamos el return tiene que estar a la altura del for!!!!!
    return cont

string = "nknnknjnjkn"
print(largoCadena(string))

def findLength(string):
    # Initialize count to zero
    count = 0
    # Counting character in a string
    for i in string:
        count+= 1
    # Returning count
    return count
# Driver code
string = "geeksforgeeks"
print(findLength(string))