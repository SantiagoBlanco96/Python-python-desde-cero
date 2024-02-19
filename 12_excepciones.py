# Excepciones
numberOne = 10
numberTwo = 6
numberTwo = "6"

# print(numberOne + numberTwo) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# try except
'''
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
'''

# try except else

# try:
#     print(numberOne + numberTwo)
#     print("No se ha producido un error")
# except:
#     print("Se ha producido un error")
# else:
#     print("La operación se ha realizado correctamente")

# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La operación se ha realizado correctamente")
finally:
    print("Esto se ejecuta siempre")
    
# try except else finally con excepciones específicas

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un error de tipo de dato")
except ValueError:
    print("Se ha producido un error de valor")
    
# try except else finally con excepciones específicas y alias

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as e:
    print(f"Se ha producido un error de tipo de dato: {e}")
except Exception as e:
    print(f"Se ha producido un error de valor: {e}")