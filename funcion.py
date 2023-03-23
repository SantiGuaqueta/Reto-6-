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

def calcular_raiz_cubica (num1:float, num2:float, num3:float, num4:float, num5:float)->float:
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