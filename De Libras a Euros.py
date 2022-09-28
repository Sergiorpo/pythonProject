#pasar de Libar a Euros
print("Este programa pasa de Libras a Euros")
libras = float(input("Dime la cantidad de libras que quieres que pase a euros: "))
valor_usuario = libras * 1.182429
print("El resultado es {}".format(valor_usuario))

#Otra firma de ponerlo seria
print("En este caso sera el usuario quien diga no solo la cifra a calcular si no a cuento esta la Libra")
libras = float(input("Dime la cantidad de Libras que tienes: "))
euros = float(input("Dime a cuanto esta la libra: "))
print("El resultado es {}".format(libras * euros))