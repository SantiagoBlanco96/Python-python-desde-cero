# Tu tarea es extender el comportamiento de la clase Stack de tal manera que la clase pueda contar todos los elementos que son agregados (push) y quitados (pop).
"""
Sigue las sugerencias:

Introduce una propiedad diseñada para contar las operaciones pop y nombrarla de una manera que garantice que esté oculta.
Inicializala a cero dentro del constructor.
Proporciona un método que devuelva el valor asignado actualmente al contador (nómbralo get_counter()).
"""

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0
    
    def get_counter(self):
        return self.__counter

    def pop(self):
        val = Stack.pop(self)
        self.__counter += 1
        return val
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())