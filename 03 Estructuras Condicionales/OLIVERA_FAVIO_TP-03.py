### ESTE ARCHIVO CORRESPONDE AL TRABAJO PRACTICO N°3 ###

"""1. Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
   deberá mostrar un mensaje en pantalla que diga "Es mayor de edad"."""

edad = int(input("Ingresa tu edad: "))
if(edad >= 18):
    print("Es mayor de edad.")
else:
    pass


"""2. Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
   mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
   mensaje “Desaprobado”."""

nota = float(input("Ingresa tu nota: "))
if(nota >= 6 and nota <= 10):
    print("Aprobado.")
elif(nota < 6 and nota >= 0):
    print("Desaprobado.")
else:
    print("Nota inválida. Debe estar entre 0 y 10.")


"""3. Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
   número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
   contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
   operador de módulo (%) en Python para evaluar si un número es par o impar."""

numero = int(input("Ingresa un número para validar si es par: "))
if(numero % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


"""4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""

edad = int(input("Ingresa tu edad: "))
if(edad < 12):
    print("Niño/a")
elif(edad >= 12 and edad <= 18):
    print("Adolescente")
elif(edad >= 18 and edad < 30):
    print("Adulto/a joven")
else:
    print("Adulto/a")