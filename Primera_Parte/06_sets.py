# Sets
"""
son colecciones desordenadas de elementos ÚNICOS.
Se utilizan para hacer pruebas de pertenencia, eliminación de entradas duplicadas 
y operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.
""" 
my_set = set()
my_other_set = {} # Esto inicialmente es un diccionario
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Juan", "Perez", 25}
print(type(my_other_set))

print(len(my_other_set)) # Longitud de un set

# No se puede acceder a un elemento de un set por posición, ya que los sets no tienen orden
# print(my_other_set[0]) # Esto da error

my_other_set.add("Python") # Agregar un elemento a un set
# my_other_set.add("Juan") No se agrega porque ya existe, solo se permiten elementos únicos

print("Python" in my_other_set) # Verificar si un elemento está en un set
print("Java" in my_other_set) # False

my_other_set.remove("Juan") # Eliminar un elemento de un set
my_other_set.discard("Juan") # Eliminar un elemento de un set, si no existe no da error
my_other_set.pop() # Eliminar un elemento de un set, no se sabe cual se va a eliminar
# my_other_set.clear() # Eliminar todos los elementos de un set
# del my_other_set # Eliminar un set

my_new_set = my_set.union(my_other_set) # Unión de sets
print(my_new_set.union(my_other_set)) # No pasa nada porque no hay elementos únicos

print(my_new_set.intersection(my_other_set)) # Intersección de sets, elementos comunes
print(my_new_set.difference(my_other_set)) # Diferencia de sets, elementos que no están en el otro set
