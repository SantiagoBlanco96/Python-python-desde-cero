# Diccionarios son estructuras de datos que permiten almacenar pares clave-valor.
# Se definen con llaves y los elementos separados por comas.

my_dict = {}
my_other_dict = dict()

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Juan", 
    "Edad": 35, 
    "Cursos": ["Python", "Django", "JavaScript"],
    1: "Hola"
}

my_dict = {"Nombre": "Juan", "Edad": 35, "Cursos": ["Python", "Django", "JavaScript"]}

print(type(my_dict["Cursos"]))
print(my_dict["Nombre"])

# Agregar un nuevo par clave-valor
my_dict["Cedula"] = 123456
print(my_dict)

# Modificar un valor
my_dict["Nombre"] = "Juan Carlos"
print(my_dict)

# Eliminar un par clave-valor
del my_dict["Cedula"]
print(my_dict)

print("Juan" in my_dict) # False
print("Nombre" in my_dict) # True

print(my_dict.items()) # Devuelve una lista de tuplas con los pares clave-valor
print(my_dict.keys()) # Devuelve una lista con las claves
print(my_dict.values()) # Devuelve una lista con los valores

my_new_dict = dict.fromkeys(my_dict) # Crea un nuevo diccionario con las claves de otro diccionario y valores por defecto None