# Modulos
# Un módulo es un archivo que contiene definiciones y declaraciones de Python.
# import 10_funciones # Importamos el módulo 10_funcione, no funciona por el nombre del archivo
import module # Importamos el módulo module

print(module.sum_two_values(5,3))

# from module import sum_two_values # Importamos la función sum_two_values del módulo module

# print(sum_two_values(5,3) # No es necesario el nombre del módulo para llamar a la función si usamos from module import sum_two_values

import math # Importamos el módulo math 

sqrt = math.sqrt(25) # Usamos la función sqrt del módulo math

print(f"La raíz cuadrada de 25 es {sqrt}")

from random import randint as ri # Importamos la función randint del módulo random con un alias, esto es útil si la función tiene un nombre muy largo