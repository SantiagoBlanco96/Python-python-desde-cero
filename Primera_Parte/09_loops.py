# Loops

# While

my_condition = 0

# while de siempre
while my_condition < 10:
    print(f"El valor de my_condition es {my_condition}")
    my_condition += 1
    
print("La ejecucción continúa...")

# while en python es como un if

my_condition = 0

while my_condition < 10:
    print(f"El valor de my_condition es {my_condition}")
    my_condition += 1
else:
    print("my_condition ya no es menor a 10")
    
my_condition = 0

while my_condition < 10:
    print(f"El valor de my_condition es {my_condition}")
    my_condition += 1
    if my_condition == 5:
        break # Termina el ciclo
else:
    print("my_condition ya no es menor a 10")

# For

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)
    
my_tuple = (1, 2, 3, 4, 5)

for element in my_tuple:
    print(element)

my_set = {1, 2, 3, 4, 5}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Juan", "Edad": 35, "Cursos": ["Python", "Django", "JavaScript"]}

for value in my_dict.values():
    print(value)

my_string = "Hola Mundo"

for char in my_string:
    print(char)
else: # Se ejecuta al finalizar el ciclo
    print("Fin del ciclo")
    
for i in range(10):
    print(i)
    if i == 5:
        break # Termina el ciclo
    
for i in range(10):
    if i == 5:
        continue # Salta a la siguiente iteración del ciclo sin ejecutar el código que sigue
    print(i)
