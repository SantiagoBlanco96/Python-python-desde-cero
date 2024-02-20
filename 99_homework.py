# Homework
"""
1 Variables y Operadores: Escribe un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero, el programa debe mostrar un error.

2 Strings: Escribe un programa que pida al usuario su nombre y muestre por pantalla el nombre en mayúsculas y el número de caracteres que contiene.

3 Listas: Escribe un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

4 Tuplas: Crea una tupla con los meses del año, pide números al usuario, si el numero está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición, si está fuera de los límites, muestra un mensaje de error.

5 Sets: Crea un set con los números del 1 al 10. Luego, pide al usuario que introduzca un número. Si el número está en el set, elimínalo y muestra el set por pantalla. Si el número no está en el set, añádelo y muestra el set por pantalla.
"""

# # 1
# print("Ejercicio 1")
# num1 = float(input("Ingrese un número: "))
# num2 = float(input("Ingrese otro número: "))
# if num2 == 0:
#     print("Error, no se puede dividir por cero")
# else:
#     print(f"La división de {num1} entre {num2} es {num1 / num2}")

# # 2 
# print("Ejercicio 2")
# name = input("Ingrese su nombre: ")
# print(f"Su nombre en mayúsculas es {name.upper()} y tiene {len(name)} caracteres")

# # 3
# print("Ejercicio 3")
# my_list = list(range(1, 11)) # range(1, 11) genera una lista de números del 1 al 10, el 11 no se incluye
# print(my_list[::-1])

# # 4
# print("Ejercicio 4")
# months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
# num = int(input("Ingrese un número: "))
# if num >= 1 and num <= len(months):
#     print(months[num - 1])
# else: 
#     print("Error, el número está fuera de los límites")

# # 5
# print("Ejercicio 5")

# my_set = set(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # set(range(1, 11))
# num = int(input("Ingrese un número: "))
# if num in my_set:
#     my_set.remove(num)
# else:
#     my_set.add(num)

# print(my_set)

# hora_inicio = float(input("Ingrese la hora de inicio: "))
# minuto_inicio = float(input("Ingrese el minuto de inicio: "))
# duracion = float(input("Ingrese la duración en minutos: "))

# hora_fin = hora_inicio + (minuto_inicio + duracion) // 60
# minuto_fin = (minuto_inicio + duracion) % 60
# hora_fin = int(hora_fin % 24)
# minuto_fin = int(minuto_fin)
# print(f"La hora de finalización es {hora_fin}:{minuto_fin}")

# En python % es el operador módulo, que devuelve el resto de la división entera
# en python // es el operador división entera, que devuelve el cociente de la división entera

# odd_numbers = 0
# even_numbers = 0

# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)

steps = 0
n = int(input("Ingrese un número natural: "))

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    steps += 1
    print(n)
print("Pasos = ", steps)
