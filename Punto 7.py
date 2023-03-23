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
