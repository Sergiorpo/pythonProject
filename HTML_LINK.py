#Metes los datos y te los guarda en un TXT con formato HTML

f = open("HTML.txt", "a")

## Variable que sirve para que el usuario pueda cerrar el bucle
salir = None
while salir != "salir":
      salir = input("Quieres continuar: ")
      ## Si escribe "salir" cierra el programa.
      if salir == "salir":
            exit()
      else:
            ## Variables.
            direccion = input("Introduce URL: ")
            nombre = input("Introduce nombre de la pagina:  ")
            descripcion = input("Escribe una descripcion de la pagina: ")
            hashtag_name = input("Introduce los Hashtag:  ")

# Muestra la salida
            print("<ol id=\""'box'"\">\n"
            "<li>\n"
            "<a href=\"", direccion, "\">", nombre, "</a>\n"
            "<p>",descripcion, "</p>\n"
            "<p id=\""'hashtag'"\">", hashtag_name, "</p>\n"
            "<li>\n"
            "<ol>\n", file=f)


#Cierra y guarda el documento
f.close()
input("Salir..")
