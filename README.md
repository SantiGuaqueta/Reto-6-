# Reto-6-
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_6 en slack.

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*
```python
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
```
[![Captura-de-pantalla-2023-03-22-205800.png](https://i.postimg.cc/zX5Tx9Tr/Captura-de-pantalla-2023-03-22-205800.png)](https://postimg.cc/Yjn49DXn)

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*
``` python
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
```

[![Captura-de-pantalla-2023-03-22-212157.png](https://i.postimg.cc/yNBFbtM9/Captura-de-pantalla-2023-03-22-212157.png)](https://postimg.cc/LJCYqC66)

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

9. Consultar qué es y cómo funciona *pip* en python.

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.


