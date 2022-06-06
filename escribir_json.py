import json

RUTA= "semana_11/config_alt.json"

def main():
	datos= {
		"id": 45,
		"cuidad": "rafaela",
		"provincia": "santa fe",
		"pais": "argentina",
		"interconectada": True
		}
	guardarconfigjson(RUTA, datos)

def guardarconfigjson(direccion, contenido):
    archivo= open(direccion, "w") #w modo escritura
    archivo.write(json.dumps(contenido))
    archivo.close()
    print ("confg actualizada")

   

#flujo principal
if (__name__=="__main__"):
   main()