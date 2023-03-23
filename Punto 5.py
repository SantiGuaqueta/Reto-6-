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