def anagrama(texto1, texto2):
    texto1 = texto1.replace(' ', '').lower()
    texto2 = texto2.replace(' ', '').lower()
    
    if sorted(texto1) == sorted(texto2):
        return 'Es un anagrama'
    else:
        return 'No es un anagrama'

texto1 = input('Ingrese la primer palabra: ')
texto2 = input('Ingrese la segunda palabra: ')

print(anagrama(texto1, texto2))