#Introduces una frase y puedes indicar en que punto quieres introducir una lista que pasaras posteriormente.



import os
import platform
def limpiar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

print("Esta aplicacion te permite escribir un texto y "
      "donde pongas  {0} sera sustituido por el nombre de usuario que te pedire mas adelante."
      "Aparte podras gardar el fichero en la extension que tu quieras.")

texto = input("Introduce un texto: ")
lista = []
lista_usuario = None
limpiar()


print("Ahora escribe el nombre de usuarios o usuarios. Puedes introducir tantos como quieras.")
while lista_usuario != "SALIR":
    lista_usuario = input("Introduzca un usuario o escriba 'SALIR' para finalizar:  ")
    if lista_usuario == "SALIR":
        print("FIN")
    if lista_usuario != "SALIR":
        lista.append(lista_usuario)







limpiar()
nombre_fichero = input("Dime el nomnre del fichero: ")
extension_archivo = input("Dime en que extension quieres que se guarde.\n"
                          "Ejemplo: Txt, Bat, xlsx, Html, PS1 etc\n"
                          "")


f = open (nombre_fichero+'.'+extension_archivo,'w')
list_user = []

for i in lista:
    list_user.append(texto.format(i))



print('\n'.join(list_user),file=f)

f.close()


input("Presiona cualquier tecla para finalizar...")