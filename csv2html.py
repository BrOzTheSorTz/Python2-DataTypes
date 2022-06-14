
import sys
from glob import escape


def main():
    maxwidth=100#Para el número máx de caracteres en una celda
    print_start() #funcion que hay que crear
    count =0
    while True:
        try:
            line =input()
            if count ==0 :
                color ="lightgreen"
            elif count %2:
                color="white"
            else:
                color ="lightyellow"

            
            print_line(line,color,maxwidth) #Otra función necesaria
        
        except EOFError:
            break

    print_end() #Otra función

def print_start():
    print("<table border='1'>")
def print_end():
    print("</table>")

def print_line(line,color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color)) #FIELD NAMES.Nos permiten identificar el color de la celda
    fields= extract_fields(line)
    for field in fields:#Creamos una fila de tabla para cada linea del archivo
        if not field:
            print("<td></td>")
        else:
            number=field.replace(",","")#Para saber como de grandes es la linea
            try:
                x=float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field=field.title()
                field =field.replace(" And "," and ")
                if len(field) <= maxwidth:
                    field =escape_html(field)
                else:
                    field = "{0}...".format(
                        escape.html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr")

#Lee la linea dada caracter por caracter 
#acumulando una lista letras
def extract_fields(line):
    fields=[]
    field=""
    quote=None

    for c in line:
        if c in "\"'":
            if quote is None:#El comienzo
                quote = c
            elif quote == c:#El final
                quote =None
            else:           #Vamos cogiendo toda la frase
                field +=c
            continue
        if quote is None and c==",":
            fields.append(field)
            field =""
        else:
            field +=c
            
    if field:
        fields.append(field) #Añadimos la útlima palabra
    return fields

#Remplaza los caracteres especiales de HTML
# con su equivalente en python 
#  
def escape_html(text):
    text =text.replace("&","&amp;")
    text=text.replace("<","&lt")
    text=text.replace(">","&gt")
    return text