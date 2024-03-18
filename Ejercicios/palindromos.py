# Palindromo: Es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.

def palindromo(palabra):
    palabra = palabra.replace(' ', '') # Eliminamos los espacios en blanco
    palabra = palabra.lower() # Convertimos la palabra en minusculas
    palabra_invertida = palabra[::-1] # Invertimos la palabra
    if palabra == palabra_invertida:
        return "Es un palíndromo."
    else:
        return "No es un palíndromo."
    
palabra = input("Ingresa una palabra o frase: ")
print(palindromo(palabra))
