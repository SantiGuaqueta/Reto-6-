# Punto 4

def vueltas(pan: int, leche: int, huevos:int, billete:float)-> float:
    vueltas_de_dinero=( billete- (pan*300 + leche*3300  + huevos*350 ))#Conocemos los valores porque el problema nos da los datos.
    return(vueltas_de_dinero)
#Planteamos la ecuacione para hallar la vuelta de dinero.

if __name__ == "__main__":
  pan = int(input("Ingrese cantidad de panes: "))
  leche = int(input("Ingrese cantidad bolsas de leche: "))
  huevos = int(input("Ingrese cantidad de huevos: "))
  billete=float(input("Ingrese cantidad del billete: "))
  vueltas_de_dinero = vueltas(pan,leche,huevos,billete)
  print("las vueltas o lo que se queda debiendo es:  " + str(vueltas_de_dinero))