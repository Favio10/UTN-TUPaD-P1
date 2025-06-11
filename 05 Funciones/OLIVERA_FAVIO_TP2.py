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

#5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    print(f"{segundos} segundos son {horas} horas")

#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

#9
def celcius_a_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius}°C son {fahrenheit}°F")

#10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")

#Programa principal

imprimir_hola_mundo()
saludar_usuario(input("Ingresá tu nombre: "))
informacion_personal(input("Ingresa tu nombre: "), input("Ingresa tu apellido: "), int(input("Ingresa tu edad: ")), input("Ingresa tu lugar de residencia: "))
calcular_area_circulo(float(input("Ingresa el radio del círculo para calcular el area: ")))
calcular_perimetro_circulo(float(input("Ingresa el radio del círculo para calcular el perímetro: ")))
segundos_a_horas(int(input("Ingresa la cantidad de segundos para convertir a horas: ")))
tabla_multiplicar(int(input("Ingresa un número para mostrar su tabla de multiplicar: ")))
operaciones_basicas(int(input("Ingresa el primer número: ")), int(input("Ingresa el segundo número: ")))
calcular_imc(float(input("Ingresa tu peso en kg: ")), float(input("Ingresa tu altura en metros: ")))
celcius_a_fahrenheit(float(input("Ingresa la temperatura en grados Celsius: ")))
calcular_promedio(float(input("Ingresa tu primer calificación: ")), float(input("Ingresa tu segunda calificación: ")), float(input("Ingresa tu tercera calificación: ")))

