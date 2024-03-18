# Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de la variable: ", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea, se puede hacer pero no es una buena práctica!!!
name, surname, alias, age = "Juan", "Perez", "JP", 25
print("me llamo:", name, surname, ". Mi edad es", age, ". Y mi alias es", alias)

# La forma correcta de definir variables en python es
name = "Juan"
surname = "Perez"
alias = "JP"
age = 25

# Inputs
name = input("Ingrese su nombre: ")
print("Hola", name)