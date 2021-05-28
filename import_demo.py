"""
File demonstrate how to import the in-built modules or classes and user defined modules
"""
from math import sqrt
import sys
import mymodule_demo

print("command line arguments")
for i in sys.argv:
    print(i)

number_sqrt = sqrt(131)
print("square root is", number_sqrt)
mymodule_demo.print_name("Nick")
