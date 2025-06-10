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



#Programa principal

imprimir_hola_mundo()
saludar_usuario(input("Ingresá tu nombre: "))
informacion_personal(input("Ingresa tu nombre: "), input("Ingresa tu apellido: "), int(input("Ingresa tu edad: ")), input("Ingresa tu lugar de residencia: "))
