"""
termino general matriz (en ingles array)
listas  :[] corchetes modificable
tuplas: () parentesis no modificable
diccionarios :llaves
"""
#lista mutable

lectura_lista= [23, 24, 21, 25, 26]

for c1 in range (5):
	print (c1)
	print(lectura_lista[c1])

# tuplas inmutable

lectura_tuplas=( 16, 15, 18, 19, 20)

for c1 in range (5):
	print (c1)
	print(lectura_tuplas[c1])

# diccionarios

datos_personales= {
	"nombre":" rafael gonzalez",
	"institucion":" adimra ",
	"saldo": 21314.22,
	"activo": True
	 }
print(datos_personales ["nombre"])

