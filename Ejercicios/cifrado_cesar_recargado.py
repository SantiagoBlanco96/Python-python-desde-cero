# Cifrado César.
text = input("Ingresa tu mensaje: ")
desplazamiento = 0

while desplazamiento == 0:
    try:
        desplazamiento = int(input("Ingresa un desplazamiento entre 1 y 25: "))
    except ValueError:
        print("El desplazamiento debe ser un número entero.")
        desplazamiento = 0
    if desplazamiento < 1 or desplazamiento > 25:
        print("El desplazamiento debe estar entre 1 y 25.")
        desplazamiento = 0
    
cipher = ''

for char in text:
    
    if char.islower() and (ord(char)+ desplazamiento) > 122:
        code = ord(char) -26 + desplazamiento
    elif char.isupper() and (ord(char)+ desplazamiento) > 90:
        code = ord(char) -26 + desplazamiento
    elif not char.isalpha():
        code = ord(char)
    else:  
        code = ord(char) + desplazamiento
                   
    cipher += chr(code)
    
print(cipher)
