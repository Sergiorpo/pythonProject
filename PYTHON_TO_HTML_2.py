#Metes los datos y te los guarda en un TXT con formato HTML

f = open("HTML_beta.txt", "a")

direccion = input("Introduce URL: ")
nombre = input("Introduce nombre de la pagina:  ")
descripcion = input("Escribe una descripcion de la pagina: ")
hashtag_name = input("Introduce los Hashtag:  ")

#Muestra la salida
print("\t<ol id=\""'box'"\">\n"
"\t\t\<li>\n"
"\t\t<a href=\"",direccion,"\">",nombre,"</a>\n"
"\t\t<p>",descripcion,"</p>\n"
"\t\t<p id=\""'hashtag'"\">",hashtag_name,"</p>\n"
"\t\t<li>\n"
"\t\t<ol>\n", file=f)

## \t y \xa0 es lo mismo


direccion = input("Introduce URL: ")
nombre = input("Introduce nombre de la pagina:  ")
descripcion = input("Escribe una descripcion de la pagina: ")
hashtag_name = input("Introduce los Hashtag:  ")

#Muestra la salida
print("\xa0<ol id=\""'box'"\">\n"
"\xa0\xa0\xa0\xa0<li>\n"
"\xa0\xa0\xa0\xa0\xa0<a href=\"",direccion,"\">",nombre,"</a>\n"
"\xa0\xa0\xa0\xa0\xa0<p>",descripcion,"</p>\n"
"\xa0\xa0\xa0\xa0\xa0<p id=\""'hashtag'"\">",hashtag_name,"</p>\n"
"\xa0\xa0\xa0<li>\n"
"\xa0<ol>\n", file=f)

f.close()
input("Salir..")

f.close()
input("Salir..")