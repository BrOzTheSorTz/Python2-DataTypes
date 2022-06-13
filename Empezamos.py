print("Hello")
a=3

#Ya sabemos que floats no se pueden comparar
#No obstante podemos compararlos con la mayor 
#precision posible de nuestro sistema

import sys
import math

def compararFloat(a,b):
    if abs(a-b) < sys.float_info.epsilon:
        print("Son iguales")
    else:
        print("Son distintos")


b=3.0000000000000000000000000000000000000001

compararFloat(a,b)
