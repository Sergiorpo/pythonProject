# Ejemplo de como hacer cual es el numero mas grande y cual es mas pequeno

print("Dime {} tres numeros y te dire cual es el mas pequenio y cual el mas grande.".format(nombre))
numero1 = int(input("Dime tu primer numero: "))
numero2 = int(input("Dime tu segundo numero: "))
numero3 = int(input("Dime tu cercer numero "))
print("El numero mas pequenio es {}".format(min(numero1,numero2,numero3)))
print("El numero mas grande es {}".format(max(numero1,numero2,numero3)))

exit = input("Pulsa cualquier tecla para salir..")
f.close()
