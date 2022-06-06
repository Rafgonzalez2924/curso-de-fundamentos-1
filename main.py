

import conf

cuenta = 0
persona = 0
giro = "horario"

if (conf.PERSONAS > conf.LIMITE_CUENTA):
  print("error")

else:
  for ciclo in range(conf.LIMITE_CUENTA):
    cuenta = cuenta + 1 #esto es un contador
    if (giro == "horario"):
      if (persona == conf.PERSONAS):
        persona = 0
      persona = persona + 1 # contador de personas
    
    else:
      if (persona == 1):
         persona = conf.PERSONAS + 1
      persona = persona - 1 # contador de personas
            
    if (cuenta % 8 == 0): #para saber si es divisible
      if ( giro == "horario"):
          giro= "antihorario"
      else:
        giro= "horario"
        
    print(persona, cuenta)
    
    if (cuenta % 11 == 0):
      if ( giro == "horario"): 
        persona = persona + 1
      if ( giro == "antihorario"):
        persona = persona - 1