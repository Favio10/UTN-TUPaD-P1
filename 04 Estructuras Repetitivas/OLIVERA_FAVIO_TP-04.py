## Práctico 4: Estructuras repetitivas
# Implementar ciclos para resolver problemas que requieran repetición de acciones.


# # 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

contador = 0
for i in range(101):
    print(contador)
    contador = contador + 1

# # 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# # dígitos que contiene.

numero = int(input("Ingrese un numero entero para contar sus digitos: "))
contador = 0
while numero > 0:
    numero = numero // 10
    contador = contador + 1


# # 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# # dados por el usuario, excluyendo esos dos valores.

print("Te solicitare dos numeros enteros para sumar todos los numeros entre ellos")
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
suma = 0
if numero1 < numero2:
    for i in range(numero1 + 1, numero2):
        suma = suma + i
else:
    for i in range(numero2 + 1, numero1):
        suma = suma + i
print("La suma de los numeros entre", numero1, "y", numero2, "es:", suma)


# # 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# # secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# # un 0.

print("Ingresa numeros para sumarlos, ingresa 0 para terminar")
suma = 0
num = int(input("Ingresa un numero: "))
while num !=0:
    suma = suma + num
    num = int(input("ingresa otro numero: "))
print("La suma total es: ", suma)


# # 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# # programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_aleatorio = random.randint(0, 9)
intentos = 0
print("Adivina el numero entre 0 y 9")
while True:
    num_usuario = int(input("Ingresa un numero: "))
    intentos = intentos + 1
    if num_usuario == num_aleatorio:
        print("Adivinistaste el numero en ", intentos, "intentos")
        break
    elif num_usuario < num_aleatorio:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    

# # 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# # entre 0 y 100, en orden decreciente.

print("Los numeros pares entre 0 y 100 son:")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# # 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# # número entero positivo indicado por el usuario.

print("Ingresa un numero entero positivo para sumar todos los numeros entre 0 y ese numero")
numer_usuario = int(input("Ingresa un numero: "))
suma = 0
for i in range(0, numer_usuario + 1):
    suma = suma + i
print(" la suma de los numeros entre 0 y ", numer_usuario, "es: ", suma)

# # 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# # programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# # negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# # menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("Ingresa 100 numeros enteros para contar cuántos son pares, impares, negativos y positivos")
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
for i in range(100):
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        contador_pares = contador_pares + 1
    else:
        contador_impares = contador_impares + 1
    if numero > 0:
        contador_positivos = contador_positivos + 1
    elif numero < 0:
        contador_negativos = contador_negativos + 1
print("La cantidad de numeros pares es: ", contador_pares)
print("La cantidad de numeros impares es: ", contador_impares)
print("La cantidad de numeros positivos es: ", contador_positivos)
print("La cantidad de numeros negativos es: ", contador_negativos)

# # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# # media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# # poder procesar 100 números cambiando solo un valor).



# # 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# # usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("Ingresa un numero para invertir sus digitos")
numero = int(input("Ingresa un numero: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10
print("El numero invertido es: ", numero_invertido) 