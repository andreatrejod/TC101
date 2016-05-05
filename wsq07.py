print ("Hoy voy a calcular un la suma entre un rango de números que tu me proporciones")
print ("Por favor dame el primer número de tu rango: ")
x= int(input())
print ("Por favor dame el segundo número de tu rango")
y=int(input())
suma=0

if x<y:
    y=y+1

    for n in range(x,y):
        suma=suma+x
        x=x+1

    print ("La suma de tu rango es: " ,suma)
else:
    x=x+1
    for n in range(x,y):
        suma=suma+y
        y=y+1
    print("La suma de tu rango es: " ,suma)
