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

# steps = 0
# n = int(input("Ingrese un número natural: "))

# while n != 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = n * 3 + 1
#     steps += 1
#     print(n)
# print("Pasos = ", steps)

# beatles= []
# print("Paso 1: ", beatles)
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Paso 2: ", beatles)
# for i in range(2):
#     beatles.append(input("Agrega a un nuevo miembro: "))
# print("Paso 3: ", beatles)
# del beatles[-1]
# del beatles[-1]
# print("Paso 4: ", beatles)
# beatles.insert(0, "Ringo Starr")
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

"""
4.3.4   LAB   Un año bisiesto: escribiendo tus propias funciones
Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

La semilla de la función ya se muestra en el código esqueleto del editor.

Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.
"""
# Mi solucion

# def is_year_leap(year):
#     if (year%4 == 0) and (not(year%100 == 0) or year%400 == 0):
#         return True
#     else:
#         return False

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")

"""
4.3.5   LAB   Cuántos días: escribiendo y usando tus propias funciones
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, 
tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. 
Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

"""

# Mi solucion

# def is_year_leap(year):
#     if (year%4 == 0) and (not(year%100 == 0) or year%400 == 0):
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_30 = [11,4,7,9]
#     if year < 1582 or month < 1 or month > 12:
#        return None
#     if month in month_30:
#         return 30
#     elif month != 2:
#         return 31
#     else:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")

"""
4.3.6   LAB   Día del año: escribiendo y usando tus propias funciones
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) 
y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. 
Esta prueba es solo el comienzo.
"""
# def is_year_leap(year):
#     if (year%4 == 0) and (not(year%100 == 0) or year%400 == 0):
#         return True
#     else:
#         return False

# def days_in_month(year, month):
    
#     month_30 = [11,4,7,9]
    
#     if year < 1582 or month < 1 or month > 12:
#        return None
       
#     if month in month_30:
#         return 30
#     elif month != 2:
#         return 31
#     else:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28

# def day_of_year(year, month, day):
    
#     total = 0
    
#     if day > days_in_month(year, month):
#         return None
#     for m in range(1,month):
#         total += days_in_month(year, m)
    
#     total += day	
#     return total

# print(day_of_year(2000, 2, 29))
"""
4.3.7   LAB   Números primos - cómo encontrarlos
Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

¿Complicado? De ningúna manera. Por ejemplo, 8 no es un número primo, ya que puedes dividirlo entre 2 y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).

Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el.

Tu tarea es escribir una función que verifique si un número es primo o no.

La función:

se llama is_prime;
toma un argumento (el valor a verificar)
devuelve True si el argumento es un número primo, y False de lo contrario.
Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y verifica el resto - si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo deberías detener el proceso.

Si necesitas conocer la raíz cuadrada de cualquier valor, puedes utilizar el operador **. Recuerda: la raíz cuadrada de x es lo mismo que x0.5.

Complementa el código en el editor.

"""
# # Solucion 1
# def is_prime(num):
    
#     num_is_prime = True
    
#     for i in range(2,num):
#         if num % i == 0:
#             num_is_prime = False
#     return num_is_prime

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()
# # Solucion 2
# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()
# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#   for event in pygame.event.get():
#    if event.type == pygame.QUIT\
#    or event.type == pygame.MOUSEBUTTONUP\
#    or event.type == pygame.KEYUP:
#     run = False

 
