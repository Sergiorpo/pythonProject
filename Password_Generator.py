import random
# Libreria para usar colores.
from colorama import Fore

# Creamos lista con todos los caracteres que queremos.
pass1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','Y','Z',
         '0','1','2','3','4','5','6','7','8','9','"','@','$','~','|','&','/','(',')','*','+','-','_','=','[',']','^']
# En este input indicamos la longitud de la clave
n = int(input("Indica la longitud de la clave: "))
# Variable password vacia.
password = ""


for i in range(n):
    password = password + random.choice(pass1)[0]

print(Fore.RED + "Tu clave es: \n",
      Fore.GREEN + password)