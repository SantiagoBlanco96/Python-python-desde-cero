# Clases

class MyEmpyPerson: # Los nombres de las clases se escriben en CamelCase es decir la primera letra de cada palabra en mayúscula
    pass

print(MyEmpyPerson)
print(MyEmpyPerson()) 

class Person:
    def __init__ (self, name, surname, alias = "Sin alias"): # El método __init__ es el constructor de la clase
        self.name = name
        self.surname = surname
        self.__alias = alias # Los atributos privados se definen con dos guiones bajos al inicio
    
    def get_alias(self):
        return self.__alias
        
    def walk (self):
        print(f"{self.name} alias {self.__alias} está caminando")

my_person = Person("Juan", "Pérez")
print(f"Nombre: {my_person.name}, Apellido: {my_person.surname}")

my_person.walk()

my_other_person = Person("María", "Gómez", "Maru")
print(f"Nombre: {my_other_person.name}, Apellido: {my_other_person.surname}, Alias: {my_other_person.get_alias()}")
my_person.alias = "Juancho"
print(f"Nombre: {my_person.name}, Apellido: {my_person.surname}, Alias: {my_person.get_alias()}")
my_other_person.walk()

