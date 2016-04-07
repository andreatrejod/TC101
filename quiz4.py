import math
print("Euler Number")
stop=int(input("Por favor dame el numero en el cual quieres que termine la secuencia "))

def euler_calc (parar):
    contador=0
    otra=0
    while(contador<=parar):
        f=math.factorial(contador)
        otra=otra+1/f
        contador=contador+1

    return otra
resultado=euler_calc(stop)
print(resultado)
