#pasar de fahrenheit a celcius
print("Este programa pasa de grados Fahrenheit a Celcius")
exit = None

while exit != "salir":
        fahrenheit = float(input("Escribe 'salir' para cerrar el programa\n"
        "Dime la cantidad que quieres que calcule: "))
        valor_usuario = (fahrenheit - 32) * 5/9
        print("El resultado es {}".format(valor_usuario))
