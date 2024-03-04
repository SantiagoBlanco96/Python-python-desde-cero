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
print(lenguaje.center(20, "-")) # Center (centra el string en una longitud determinada) y si el espacio es pequeño lo rellena con el caracter que se le pase
lenguaje.endswith("n") # Endswith (verifica si el string termina con una letra determinada) imprime True o False
lenguaje.startswith("P") # Startswith (verifica si el string comienza con una letra determinada) imprime True o False
lenguaje.isalnum() # Isalnum (verifica si el string es alfanumérico) imprime True o False
lenguaje.isalpha() # Isalpha (verifica si el string es alfabético) imprime True o False
lenguaje.isdigit() # Isdigit (verifica si el string es numérico) imprime True o False
lenguaje.islower() # Islower (verifica si el string está en minúsculas) imprime True o False
lenguaje.isupper() # Isupper (verifica si el string está en mayúsculas) imprime True o False
lenguaje.isspace() # Isspace (verifica si el string está compuesto por espacios) imprime True o False
lenguaje.istitle() # Istitle (verifica si el string está en formato de título) imprime True o False
lenguaje.lstrip() # Lstrip (elimina los espacios en blanco a la izquierda)
lenguaje.replace("P", "J") # Replace (reemplaza una letra por otra)
lenguaje.rfind("t") # Rfind (busca la última aparición de una letra) imprime la posición de la letra
lenguaje.rstrip() # Rstrip (elimina los espacios en blanco a la derecha)
lenguaje.strip() # Strip (elimina los espacios en blanco a ambos lados)
lenguaje.swapcase() # Swapcase (intercambia mayúsculas por minúsculas y viceversa)
lenguaje.title() # Title (pone en formato de título)