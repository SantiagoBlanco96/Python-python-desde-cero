### Challenges ###

"""
EL FAMOSO FIZZBUZZ:
Escribe un programa que muestre en pantalla los números del 1 al 100, pero aplicando las siguientes condiciones:
- Si el número es múltiplo de 3, muestra en pantalla "Fizz" en lugar del número
- Si el número es múltiplo de 5, muestra en pantalla "Buzz" en lugar del número
- Si el número es múltiplo de 3 y 5, muestra en pantalla "FizzBuzz" en lugar del número
"""
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")

# fizzbuzz()

"""
Escribe un programa que imprima los 50 primeros números de la serie de Fibonacci empezando por 0.
La serie de Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores.
"""

def fibonacci():
    a = 0
    b = 1
    for i in range(50):
        print(a)
        a, b = b, a + b

# fibonacci()

"""
Escribe un programa que reciba un número y determine si es un número primo.
"""

def is_prime(num):
    if num < 2:
        return False
    for a in range(2, num):
        if num % a == 0:
            return False
    return True

