print("GENERADOR DE CONTRASEÑAS")

print("\n Contraseña #1")
color = input("Elegi un Color: ")
num1 = input("Numero favorito #1 : ")
num2 = input("Numero favorito #2 : ")
CiudadFavorita = input("Ciudad Favorita: ")

ContraseñaFin = color + num1 + CiudadFavorita + num2

#----------------------------------

print("\n Contraseña #2")

import random
from typing import Concatenate

randomm = random.randint(1, 1000)
randomm1 = random.randint(1, 1000)
random = str(randomm)
random1 = str(randomm1)

ColorNum = (len(color))
CiudadFavNum = (len(CiudadFavorita))

ColorNum = str(ColorNum)
CiudadFavNum = str(CiudadFavNum)

ContraseñaFin2 = (random + color + ColorNum + "&%" + CiudadFavorita +
                  CiudadFavNum + random1)
print(
    "\n Tomara dos numeros random desde el 1 hasta el 1000, de esta forma creara una \n nueva contraseña que se junte con lka primera"
)

#----------------------------------

print("\n CONTRASEÑA")
print("Contraseña #1: ", ContraseñaFin)
print("Contraseña #2: ", ContraseñaFin2)
