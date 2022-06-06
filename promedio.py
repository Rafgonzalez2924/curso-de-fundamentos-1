CTD_LECTURAS= 5
LECTURAS = [22.3, 23.5, 23.1, 23.8, 23.1]

acumulado = 0
promedio = 0

for lectura in LECTURAS:
	acumulado=  acumulado + lectura #acumulador

promedio= acumulado / CTD_LECTURAS

print("promedio lectura:", promedio)
print ("lecturas antes:", LECTURAS)
LECTURAS.sort()
print("lecturas despues:", LECTURAS)
print ("lecturas minima:",LECTURAS[0])
