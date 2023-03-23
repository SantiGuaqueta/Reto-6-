# Punto 2
from math import pi # Importamos la constante pi con el modulo math para las operaciones 

def area_perimetro_de_la_figura(radio_circulo: float, base_rectangulo: float, altura_rectangulo:float)-> float:
    area=(base_rectangulo*altura_rectangulo)+(pi * radio_circulo**2)+(pi*radio_circulo**2)
    perimetro =((2*base_rectangulo)+(2* altura_rectangulo))+ (2*pi * radio_circulo)+(2* pi *radio_circulo)
    return(area,perimetro)
# Para hallar area o perimetro se puede buscan las formulas y las colocamos como podemos observar

if __name__ == "__main__":
  radio_circulo = float(input("Ingrese el radio de la esfera en cm: "))
  base_rectangulo = float(input("Ingrese base del rectangulo en cm: "))
  altur_arectangulo = float(input("Ingrese altura del rectangulo en cm: "))
  area,perimetro = area_perimetro_de_la_figura(radio_circulo,base_rectangulo,altur_arectangulo )
  print("El area de la figura es " + str(area))
  print("el volumen de la figura es " +str(perimetro))