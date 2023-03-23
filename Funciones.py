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