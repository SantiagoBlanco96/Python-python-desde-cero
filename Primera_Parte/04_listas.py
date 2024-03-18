# Listas -> es una estructura de datos que permite almacenar una colección de elementos. Es una forma de agrupar datos.

my_list = []
my_other_list = list()

my_list = [35, 24, 30, 17, 40, 50, 64]

print(len(my_list)) # Longitud de una lista

my_other_list = [35, "Hola", True, 3.14, [1, 2, 3]] # Las listas pueden contener cualquier tipo de dato
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

my_other_list.append(25) # Agregar un elemento al final de la lista
print(my_other_list)
my_other_list.insert(2, "Python") # Agregar un elemento en una posición específica
print(my_other_list)
my_other_list.remove(35) # Eliminar un elemento de la lista
print(my_other_list)
my_other_list.pop() # Eliminar el último elemento de la lista
my_other_list.pop(2) # Eliminar un elemento en una posición específica 
print(my_other_list.pop()) # Eliminar el último elemento de la lista y retornarlo

my_new_list = my_list.copy() # Copiar una lista
my_list.clear() # Eliminar todos los elementos de la lista
del my_other_list # Eliminar un elemento en una posición específica, no es lo mismo que clear porque elimina la lista
print(my_new_list.reverse()) # Invertir el orden de la lista
my_new_list.sort() # Ordenar la lista de menor a mayor
my_new_list.sort(reverse=True) # Ordenar la lista de mayor a menor
print(my_new_list[1:3]) # Sublista (slice) de una lista