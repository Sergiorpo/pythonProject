# Modifica el valor introducido y te lo copia directamente al portapapeles de Windows

import xerox
salir = None

while salir != "salir":
    input_usuario = input("Introduzca una fecha: ")
    final = input_usuario.replace('-', '/')
    xerox.copy(final)