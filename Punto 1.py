# Primer punto
from math import pi # Importamos la constante pi con el modulo math para las operaciones 
def area_volumen_superficial_de_la_figura(radio_esfera: float, radio_cono: float, altura:float)-> float:
    area=(4*pi*radio_esfera**2)+((pi * radio_cono**2 + pi * radio_cono * (altura**2 + radio_cono**2)** 0.5 ))
    volumen=((4/3) * pi * radio_esfera**3)+(((pi * radio_cono**2 * altura) / 3))
    return(area,volumen)
# Para hallar area o volumen se puede buscan las formulas y las colocamos como podemos observar

if __name__ == "__main__":
  radio_esfera = float(input("Ingrese el radio de la esfera en cm: "))
  radio_cono = float(input("Ingrese el radio del cono en cm: "))
  altura = float(input("Ingrese altura del cono en cm: "))
  area,volumen = area_volumen_superficial_de_la_figura(radio_esfera,radio_cono, altura)
  print("El area de la figura es " + str(area))
  print("el volumen de la figura es " +str(volumen))