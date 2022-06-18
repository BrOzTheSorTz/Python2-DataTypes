#instalamos la librería panda
# pip install pandas

import pandas

archivo=pandas.read_csv("ejemplo.csv")

archivo.to_html("Tabla.htm") #Creamos el archivo html


