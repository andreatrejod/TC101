import math #importamos este módulo para poder hacer la función
def distancia(x1, x2, y1, y2):
    dist = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2)) ##math.sqrt nos permite sacarle la raíz cuadrada a la fórmula
    print("La distancia calculada es" ,(round(dist,2)) , "unidades")


distancia(x1=int(input("Inserta el valor para X1: ")), y1=int(input("Inserta el valor para Y1: ")),
          x2=int(input("Inserta el valor para X2: ")), y2=int(input("Inserta el valor para Y2: ")))
