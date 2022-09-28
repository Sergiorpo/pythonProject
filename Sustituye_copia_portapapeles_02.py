# Otro ejemplo de como modifica el valor introducido y que te lo copia directamente al portapapeles de Windows

import xerox
salir = None

while salir != "salir":


    dia = int(input("introduce dia: "))
    mes = int(input("Introduce mes:  "))

    if mes==1:
        mes_user = "Jan"
    if mes==2:
        mes_user = "Feb"
    if mes==3:
        mes_user = "Mar"
    if mes==4:
        mes_user = "Apr"
    if mes==5:
        mes_user = "May"
    if mes==6:
        mes_user = "Jun"
    if mes==7:
        mes_user = "Jul"
    if mes==8:
        mes_user = "Aug"
    if mes==9:
        mes_user = "Sep"
    if mes==10:
        mes_user = "Oct"
    if mes==11:
        mes_user = "Nov"
    if mes==12:
        mes_user = "Dec"
    if salir == "salir":
        print(quit)
        quit()

    anio = int(input("Introduce anio: "))
    xerox.copy(u'{} {}, {}'.format(mes_user,dia,anio))




input("Pulsa para continuar..")
