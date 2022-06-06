import json

RUTA= "semana_11/clima_rafaela.json"


def recurarconfigjson(direccion):
    archivo= open(direccion, "r") #r solo lectura
    config= json.load(archivo)
    archivo.close()
    return config


def main():

    CONFG= recurarconfigjson(RUTA)
    print(CONFG["weather"][0]["description"])

#flujo principal
if (__name__=="__main__"):
   main()