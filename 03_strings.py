# Strings
my_string = "My String"
my_other_string = 'My other string'

print(len(my_string)) # Longitud de un string
print(my_string + " " + my_other_string) # Concatenación de strings

my_new_line_string = "My new line string\n con salto de línea"
print(my_new_line_string)
my_tab_string = "My tab string\t con tabulación"
print(my_tab_string)
my_scaped_string = "My scaped string \\ con barra invertida \\n" # Para escapar un caracter se usa \
    
# Formateo
name, surname, age = "Juan", "Perez", 25
print("Me llamo {} {}".format(name, surname)) # Formateo de strings
print("Mi nombre es %s y tengo %d años" %(name, age)) # Formateo de strings con %s y %d
print(f"Me llamo {name} {surname} y tengo {age} años") # Formateo de strings con f-string

# Desempaquetado de caracteres (su funcion es asignar cada caracter a una variable)
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)

# División de strings

lenguaje_slice = lenguaje[1:3] # esto imprime yt
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2] # esto imprime la penultima letra
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2] # esto imprime pto (el 2 es el salto)
print(lenguaje_slice)

# Reverse 
reversed_lenguaje = lenguaje[::-1] # esto invierte el string 
print(reversed_lenguaje)

# Funciones
print(lenguaje.capitalize()) # Capitalize (pone la primera letra en mayúscula)
print(lenguaje.upper()) # Upper (pone todo en mayúscula)
print(lenguaje.lower()) # Lower (pone todo en minúscula)
print(lenguaje.replace("P", "J")) # Replace (reemplaza una letra por otra)
print(lenguaje.count("P")) # Count (cuenta cuantas veces aparece una letra)
print(lenguaje.find("t")) # Find (busca la primera aparición de una letra) imprime la posición de la letra