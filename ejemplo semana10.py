""" modo w: write: escritiura, si el archivo no existe lo crea y si existe lo trunca, es decir lo limpia y luegolo guarda
    modo r:  read: lectura abre solo para lectura
    modo a: append: añadir, s el archivo no existe lo crea y lo añade al final
    txt: texto plano
    csv: comma separated values
    json: javascript object notation (formato muy stadnda de intercambio)
    xml: extended markup language
    """

from re import A


def guardar_cadena(cadena):
    
    archivo= open("cadena_formateada.txt", "w") #modo W= write= escritura
    archivo.write(cadena)
    archivo.close()
    print("se ha guardado la cadena en el archivo")

    pass

def recuperar_cadena():
    archivo= open("cadena_formateada.txt", "r") #modo r= read= lectura
    archivo.read()
    archivo.close()
    print("lectura")




#flujo principal
if (__name__=="__main__"):
    apellido= "Perez"
    nombre="Juan"
    edad= 18
    saldo= 15480.815

    cadena_formateada= F"cadena de ejemplo : {apellido.upper()}, {nombre}, edad: {edad}, saldo: $ {saldo} AR"
    
    #guardar_cadena(cadena_formateada)
    recuperar_cadena ()