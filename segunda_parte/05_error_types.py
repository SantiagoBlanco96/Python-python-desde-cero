### Error Types ###

# Syntax Error
# print "Hello World"

# Name Error
# print(hello)

# index Error
my_list = ["python", "java", "c++", "kotlin"]
# print(my_list[4]) # IndexError: list index out of range

# Module Not Found Error
# import maths # ModuleNotFoundError: No module named 'maths'
import math

# Attribute Error
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'
print(math.pi)

# key Error
my_dict = {"name": "John", "age": 25}
# print(my_dict["surname"]) # KeyError: 'sername'

# Type Error
# print("Hello" + 5) # TypeError: can only concatenate str (not "int") to str

# Import Error
# from math import cube # ImportError: cannot import name 'cube' from 'math'