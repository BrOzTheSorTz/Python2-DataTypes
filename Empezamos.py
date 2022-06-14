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
#Concatenar en python

testo =("Erase una vez"
        "En un Bosque"
        "Un leon muy enfadado")

#Obtener un vector de palabras a partir de un string
#con palabras separadas por algo

caracteristicas="alto;guapo;feo;tonto;listo"
palabras = caracteristicas.split(";")
print (palabras)

#Field Names

#Ejemplo1
print("{0}{1}".format("The amount due is $",200))
#Ejemplo2

x="Three"
s="{0} {1} {2}"
s=s.format("The",x,"tops")
print(s)

#Ejemplo 3

s="{who} turned {age} this year".format(who="She",age=88)
print(s)

s= "The {who} was {0} last week".format(12,who="Boy")
print(s)

#Ejemplo 4

d= dict(animal="elephant",weight=12000)
print("The {0[animal]} weighs {0[weight]} kg".format(d))

#Leer un archivo en csv y pasarlo a formato html

#Para ello primero necesitamos el archivo
#después utilizaremos csv2html.py(Para ello hay que crearlo)

#necesitaremos ejecutar lo siguiente en la terminal
# csv2html.py < nombreArchivo.csv > nuevoNombre.html

