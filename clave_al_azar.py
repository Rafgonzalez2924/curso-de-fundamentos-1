"""paradigma
PS: secuencial
PF: funcional
POO: programacion orientada a objetos"""

from ast import Pass
import random
import string





#constante
CTD_CARACTERES= 8
CTD_CLAVES=5

#funciones
def generar_clave():
    clave= ""
    for c in range (CTD_CARACTERES):
        #caracter al azar= rando.choice abcdefgh...
        caracter_al_azar= random.choice (string.ascii_letters + string.digits)
        clave= clave + caracter_al_azar #concatenar
    
    #salida
    print (clave)
#proceso
for i in range (CTD_CLAVES):
    generar_clave()
    print("---")
   
