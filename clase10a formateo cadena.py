def main ():
    apellido= "pepim"
    nombre="pepe"
    edad= 40
    saldo= 15480.815

    #opcion 1:la propia funcion print concantena los argumentos
    print ("cadena de ejemplo", apellido, ":", nombre, edad)

    #opcion 2: conectar previamente la cadena
    cadena= "cadena de ejemplo: " + apellido + ", " + nombre + str (edad)

    print(cadena)

    #opcion 3: utilizar las utilidades formar o la macro f

    cadena_formateada= F"cadena de ejemplo : {apellido}, {nombre}, edad: {edad}, saldo: $ {saldo} AR"
    print (cadena_formateada)

#flujo principal
if (__name__=="__main__"):
    main ()

