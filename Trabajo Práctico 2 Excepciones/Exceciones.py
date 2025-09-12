'''#ZeroDivision 1

try:
    a = 10
    b = 0
    resultado = a / b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")


#TypeError 2

try:
    resultado = 5 + "hola"
    print("El resultado es:", resultado)
except TypeError:
    print("Error: No se puede sumar un número y un texto.")

#KeyError 3

diccionario = {"nombre": "Juan", "edad": 30}

try:
    valor = diccionario["apellido"]
    print("El valor es:", valor)
except KeyError:
    print("Error: Esa clave no existe en el diccionario.")

#fileNotFoundError 4

try:
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe. Creando uno nuevo...")
    with open("archivo_inexistente.txt", "w") as f:
        f.write("Archivo creado automáticamente.\n")

#ValueError 5

try:
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    resultado = a / b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debe ingresar solo números.")'''

