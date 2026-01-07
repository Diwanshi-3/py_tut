import diwanshi as d  #import other file 
d.name()
d.city()
from math import sqrt as s  #import sqrt method from math module using from keyword
print(s(9))
from math import *  #import math module and its all variables and functions in program 
sqrt(9)
# math.sqrt # If we use 'from math import *', then we do NOT need to use 'math.' keyword
import math    #import module 
math.sqrt(9)   #use math. for access the method of math module in program
print(dir(math)) #print all the method of module 
#print(help(math))  #tell is function is built in or user defined or file but give very large output so donot recommended 
import sys
print('random' in sys.builtin_module_names)   #check module is built in or not 
import random
print(random.__file__)
import math
print(hasattr(math, '__file__'))  #hasattr checks if the attribute present in object or not 



