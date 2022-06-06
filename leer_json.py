import json

RUTA= "semana_11/config.json"

def main():
    recurarconfigjson()

def recurarconfigjson():
    archivo= open(RUTA, "r") #r solo lectura
    config= json.load(archivo)
    archivo.close
   # print(type(config))
   # print(config)
    print(config["ciudad"])

#flujo principal
if (__name__=="__main__"):
   main()
