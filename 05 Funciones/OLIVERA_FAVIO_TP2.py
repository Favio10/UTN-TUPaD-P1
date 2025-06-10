#Funciones
#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4
def calcular_area_circulo(radio):
    import math
    area = math.pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area}")

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    print(f"El perímetro del círculo con radio {radio} es: {perimetro}")


#Programa principal

imprimir_hola_mundo()
saludar_usuario(input("Ingresá tu nombre: "))
informacion_personal(input("Ingresa tu nombre: "), input("Ingresa tu apellido: "), int(input("Ingresa tu edad: ")), input("Ingresa tu lugar de residencia: "))
calcular_area_circulo(float(input("Ingresa el radio del círculo para calcular el area: ")))
calcular_perimetro_circulo(float(input("Ingresa el radio del círculo para calcular el perímetro: ")))