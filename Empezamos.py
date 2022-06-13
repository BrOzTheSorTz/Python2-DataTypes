print("Hello")
a=3

#Ya sabemos que floats no se pueden comparar
#No obstante podemos compararlos con la mayor 
#precision posible de nuestro sistema

import sys
import math

def compararFloat(a,b):
    #epsilon es la menor diferencia que nuestra maquina puede detectar
    if abs(a-b) < sys.float_info.epsilon:
        print("Son iguales")
    else:
        print("Son distintos")

a=1/3
b=1/3

compararFloat(a,b)

#Escribir al revés

s="Hola que tal estas"
sAlReves=s[::-1]# s[start:end:step]
print(s,"\n",sAlReves)

#------

palabras =["Hoy","Hace","Mucha","Calor"]

conEspacios = " ".join(palabras)
print(conEspacios)
conGuion ="--".join(palabras)
print(conGuion)