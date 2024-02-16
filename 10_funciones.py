# Funciones

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(a, b):
    return a + b

print(sum_two_values(5, 3))
print(sum_two_values(10, 20))

def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(surname="Pérez", name="Juan") # Podemos pasar los argumentos en cualquier orden

def print_name_with_default(name, surname, alias = "Sin alias"): # Podemos definir valores por defecto
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Juan", "Pérez")

def print_texts (*text): # Podemos pasar una cantidad variable de argumentos
    print (text)

print_texts("Hola", "Mundo", "Python")

def print_upper_text(*texts):
    for text in texts:
        print(text.upper())

print_upper_text("Hola", "Mundo", "Python")
    