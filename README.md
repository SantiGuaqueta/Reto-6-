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
  print("el perimetro de la figura es " +str(perimetro))
```

[![Captura-de-pantalla-2023-03-23-071350.png](https://i.postimg.cc/ydc2wfYR/Captura-de-pantalla-2023-03-23-071350.png)](https://postimg.cc/MMZsBmBZ)

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
``` python
# Punto 3

def cantidad_de_carne_de_aves(gallinas: int, gallos: int, pollitos:int)-> int:
    aves=(gallinas+gallos+pollitos)#agrege la cantidad de aves auqneu no es necesario fue por gusto.
    cantidad_de_carne=(6*gallinas + 7* gallos+ 1* pollitos)#Conocemos que las gallinas pesan 6kg los gallos 7kg y los pollitos 1kg.
    return(aves,cantidad_de_carne)
#Planteamos la ecuaciones para hallar la cantidad de carne.

if __name__ == "__main__":
  gallinas = int(input("Ingrese cantidad de gallinas: "))
  gallos = int(input("Ingrese cantidad de gallos: "))
  pollitos = int(input("Ingrese cantidad de pollitos: "))
  aves,cantidad_de_carne = cantidad_de_carne_de_aves(gallinas, gallos, pollitos )
  print("la cantidad de aves es:  " + str(aves))
  print("La cantidad de carne en kg es: " +str(cantidad_de_carne))
```

[![Captura-de-pantalla-2023-03-23-072859.png](https://i.postimg.cc/hjWH4GgJ/Captura-de-pantalla-2023-03-23-072859.png)](https://postimg.cc/zL7d08y5)

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
``` python
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
```

[![Captura-de-pantalla-2023-03-23-073808.png](https://i.postimg.cc/qBPqysLS/Captura-de-pantalla-2023-03-23-073808.png)](https://postimg.cc/c6cdN8PB)


5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.
``` python
# Punto 5

def valor_prestamo(dinero: float, tasa_de_interes: float, meses:int )-> float:
    intereses= tasa_de_interes/100 # lo dividimos entre 100 para quitar el porcentaje
    interes_compuesto=(1+intereses/12)**meses 
    calculo_valor_del_prestamo=( dinero * interes_compuesto)
    return(calculo_valor_del_prestamo)
#Planteamos la ecuaciones para hallar el calculo del valor del prestamo.

if __name__ == "__main__":
  dinero = float(input("Ingrese el valor del prestamo: "))
  tasa_de_interes = float(input("Ingrese la tasa de interes(sin %): "))
  meses = int(input("Ingrese cantidad de meses para pagar: "))
  calculo_valor_de_prestamo = valor_prestamo(dinero,tasa_de_interes,meses)
  print("el valor del prestamo al final es:  " + str(calculo_valor_de_prestamo))
```

[![Captura-de-pantalla-2023-03-23-083507.png](https://i.postimg.cc/SN49ng9T/Captura-de-pantalla-2023-03-23-083507.png)](https://postimg.cc/DmC0DdBL)



6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
``` python
# Punto 6

def contagiados_de_covid(dias: int, personas_contagiadas: int )-> int:
    contagiados=(2*personas_contagiadas*dias)
    return(contagiados)
#Planteamos las operaciones para hallar las personas contagiadas.

if __name__ == "__main__":
  dias = int(input("Ingrese los dias que han pasado: "))
  personas_contagiadas = int(input("Ingrese cantidad de personas contagiadas: "))
  contagiados = contagiados_de_covid(dias,personas_contagiadas)
  print("El número total de personas contagiadas después de " +str(dias)+ " días es: "+str(contagiados))
```

[![Captura-de-pantalla-2023-03-23-085618.png](https://i.postimg.cc/Z5PRNmrX/Captura-de-pantalla-2023-03-23-085618.png)](https://postimg.cc/VJ6my3ZF)



7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número
``` python
# Punto 7

def calcular_mediana(n1:float, n2:float, n3:float, n4:float, n5:float)-> float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1

    return n3

def calcular_promedio (n1:float, n2:float, n3:float, n4:float, n5:float)->float:
    promedio = (n1+n2+n3+n4+n5)/5
    return (promedio)

def calcular_promedio_multiplicativo (n1:float, n2:float, n3:float, n4:float, n5:float)->float:
    promedio_multiplicativo= (n1*n2*n3*n4*n5)**(1/5)
    return (promedio_multiplicativo)
 
def ordenar_numeros_ascendete(n1:float, n2:float, n3:float, n4:float, n5:float)->float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1

    return n1, n2, n3, n4, n5

def ordenar_numeros_descendete (n1:float, n2:float, n3:float, n4:float, n5:float)->float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1

    return n5, n4, n3, n2, n1

def calcular_potencia (n1:float, n2:float, n3:float, n4:float, n5:float)->float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1

    return (n5)**(n1)

def calcular_raiz_cubica (n1:float, n2:float, n3:float, n4:float, n5:float)->float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1

    return (n1)**(1/3)
if __name__ == "__main__":
 n1 = float(input("Ingrese el primer número: "))
 n2 = float(input("Ingrese el segundo número: "))
 n3 = float(input("Ingrese el tercer número: "))
 n4 = float(input("Ingrese el cuarto número: "))
 n5 = float(input("Ingrese el quinto número: "))
 m = calcular_mediana(n1,n2,n3,n4,n5)
 promedio= calcular_promedio(n1,n2,n3,n4,n5)
 promedio_multipicativo= calcular_promedio_multiplicativo(n1,n2,n3,n4,n5)
 oa= ordenar_numeros_ascendete(n1,n2,n3,n4,n5)
 od= ordenar_numeros_descendete(n1,n2,n3,n4,n5)
 pot= calcular_potencia(n1,n2,n3,n4,n5)
 r= calcular_raiz_cubica(n1,n2,n3,n4,n5)
print("El promedio es:" +str(promedio))
print("La mediana es:" +str(m))
print ("El promedio multiplicativo: " +str(promedio_multipicativo))
print ("Los numeros ordenados de forma ascendente son:"+str(oa))
print ("Los numeros ordenados de forma descendente son:" +str(od))
print ("La potencia del número mayor elevado al menor es: " +str(pot))
print ("La raíz cúbica del menor número es: " +str(r))

```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
```python
from funcion import calcular_mediana
from funcion import calcular_promedio
from funcion import calcular_promedio_multiplicativo
from funcion import ordenar_numeros_ascendete
from funcion import ordenar_numeros_descendete
from funcion import calcular_potencia
from funcion import calcular_raiz_cubica

if __name__ == "__main__":
 n1 = float(input("Ingrese el primer número: "))
 n2 = float(input("Ingrese el segundo número: "))
 n3 = float(input("Ingrese el tercer número: "))
 n4 = float(input("Ingrese el cuarto número: "))
 n5 = float(input("Ingrese el quinto número: "))
 m = calcular_mediana(n1,n2,n3,n4,n5)
 promedio= calcular_promedio(n1,n2,n3,n4,n5)
 promedio_multipicativo= calcular_promedio_multiplicativo(n1,n2,n3,n4,n5)
 oa= ordenar_numeros_ascendete(n1,n2,n3,n4,n5)
 od= ordenar_numeros_descendete(n1,n2,n3,n4,n5)
 pot= calcular_potencia(n1,n2,n3,n4,n5)
 r= calcular_raiz_cubica(n1,n2,n3,n4,n5)
print("El promedio es:" +str(promedio))
print("La mediana es:" +str(m))
print ("El promedio multiplicativo: " +str(promedio_multipicativo))
print ("Los numeros ordenados de forma ascendente son:"+str(oa))
print ("Los numeros ordenados de forma descendente son:" +str(od))
print ("La potencia del número mayor elevado al menor es: " +str(pot))
print ("La raíz cúbica del menor número es: " +str(r))
```
[![Captura-de-pantalla-2023-03-23-113026.png](https://i.postimg.cc/B6wdSYw6/Captura-de-pantalla-2023-03-23-113026.png)](https://postimg.cc/Q916SbDG)


9. Consultar qué es y cómo funciona *pip* en python.

Pip en python es un sistema de gestión de paquetes manejado para instalar y administrar paquetes de software escritos en Python y descargarlos a nuestra computadora con el propósito de integrarlos a nuestros desarrollos realizado en python. Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto; lo cual no es necesario instalarlo en nuestra pc ya que al instalar python en la version 3.4 o superior en automático se instala el gestor de paquetes.
PIP es un acrónimo que significa "Paquetes de instalación PIP" o "Programa de instalación preferida". Es una utilidad de línea de comandos que le permite instalar, reinstalar o desinstalar paquetes PyPI con un comando simple y directo: "pip".
#### Cómo instalar PIP en Windows
Las siguientes instrucciones deberían funcionar en Windows 7, Windows 8.1 y Windows 10:

Descargue el script del instalador get-pip.py. Si estás en Python 3.2, necesitarás esta versión de get-pip.py. En caso de tener Python 3.3 o 3.4 usar estas versiones de PiP correspondientemente Python 3.3 get-pip.py o Python 3.4 get-pip.py. De cualquier manera, haga clic derecho en el enlace y seleccione Guardar como y guárdelo en cualquier carpeta del pc, como su carpeta de Descargas.

Abra el símbolo del sistema y navegue hasta el archivo get-pip.py.

Ejecute el siguiente comando: python get-pip.py

📝 Nota: Ejecutar la terminal (CMD o Powershell) con privilegios de administrador
bibliografia

#### Cómo actualizar PIP para Python
Si tuvieramos una versión anterior o muy viejita instalada de pip en nuestra computadora y quisieramos tener la última versión con la finalidad de descargar también las últimas versiones de librerias que se encuentran en los repositorios de python se puede hacer si ningun problema.

PIP no es una aplicación que se actualice muy a menudo. Sin embargo, no por ello es menos importante hacer uso de las nuevas versiones cuando están disponibles, ya que además de corregir errores y problemas de compatibilidad, también pueden corregir posibles agujeros de seguridad. Actualizar Pip en python es muy sencillo:
Para actualizar PIP en Windows utiliza el siguiente comando:

python -m pip install -U pip

##### Bibliografia

PIP en Python Administrador de Paquetes PIP en Python. (s. f.). Grupo Codesi trainig & certification. Recuperado 23 de marzo de 2023, de https://www.buscaminegocio.com/cursos-de-python/pip-en-python.html

Fernandez, D. P. (2022, 7 noviembre). ¿Cómo instalar PIP para Python en Windows, Mac y Linux? 【PASO A PASO】. Tecnonucleous. https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.


