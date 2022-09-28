# El Script genera un numero aleatorio y tienes que adivinarlo.

import random

quieres = input("Quieres jugar?: ")
if quieres == "SI" or quieres == "s" or quieres == "S" or quieres == "yes" or quieres == "YES":
    usuario = int(input("Escribe un numero del 1 al 6: "))

    ganador = random.randint(1, 6)

    if usuario == ganador:
        print("GANASTE")
    if usuario > 334:
        print("Te has pasado 8 pueblos")
    if usuario > 6:
        print("Te has pasado")
    if usuario < 1:
        print("Demasiado pequeno")
    else:
        print("El numro ganador era {}".format(ganador))
        print("Loooser")
else:
    print("Otro dia quizas")