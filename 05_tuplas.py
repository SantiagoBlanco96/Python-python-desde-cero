# Tuplas 
"""
 es una estructura de datos que permite almacenar una colección de elementos. 
 Es una forma de agrupar datos. A diferencia de las listas, las tuplas son inmutables, 
 es decir, no se pueden modificar después de su creación. Se definen con paréntesis y los elementos separados por comas.
"""
my_tuple = ()
my_other_tuple = tuple()

my_tuple = (35, 24, 30, 17, 40, 50, 64)
my_other_tuple = (35, "Hola", True, 3.14, [1, 2, 3]) # Las tuplas pueden contener cualquier tipo de dato

print(my_other_tuple)

print(len(my_tuple)) # Longitud de una tupla
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3]) # Subtupla (slice) de una tupla
print(my_tuple.count(35)) # Count (cuenta cuantas veces aparece un elemento)
print(my_tuple.index(35)) # Index (busca la primera aparición de un elemento) imprime la posición del elemento

