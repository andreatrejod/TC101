print("And here it comes Fibonacci series")
print("Please give the number your want in Fibonacci series:")
numero=int(input())

def fibonacci (numero):
    inicio=1
    ultimo=0
    penultimo=0
    contador=1
    if (numero==0):
        inicio=0

    while (contador<numero):
        penultimo= ultimo
        ultimo= inicio
        inicio=penultimo+ultimo
        contador= contador+1

    return inicio
resultado= fibonacci(numero)

print ("The number",numero,"in fibonacci is:",resultado)
