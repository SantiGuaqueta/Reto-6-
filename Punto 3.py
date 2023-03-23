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