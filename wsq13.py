import math

x1=int(input("Ingresa el valor de X1: "))
y1= int(input("Ingresa el valor de Y1: "))
x2= int(input("Ingresa el valor de X2: "))
y2= int(input("Ingresa el valor de Y2: "))

def distance(x1,y1,x2,y2):
    p=math.sqrt ((x2-x1)**2+(y2-y1)**2)
    return p

print ("The distance between the points you give is",distance(x1,y1,x2,y2))

#Problem2
import os
os.system ("clear")

num=int(input("Please give me the size of your triangle: "))

def triangle (var):
    r=range(1,var)
    r2=range(var,0,-1)

    for x in r:
        result="T"*x
        print(result)

    for y in r2:
        other="T"*y
        print(other)


triangle(num)

#Problem3
import os
os.system ("clear")
a=int(input("Please give me the number of the base: "))
b=int(input("Give me the number of the pow: "))

def superpower():
	if b==0:
		return 1
	else:
	  x=1
	  y=a
	  while x<b:
	    y=y*a
	    x=x+1
	  return y

print("The result is: ", superpower())

#Problem4
print("And here it comes Fibonacci series")
print("Please give the number your want in Fibonacci series:")
number=int(input())

def fibonacci (numero):
    inicio=1
    ultimo=0
    penultimo=0
    contador=1
    if (number==0):
        inicio=0

    while (contador<number):
        penultimo= ultimo
        ultimo= inicio
        inicio=penultimo+ultimo
        contador= contador+1

    return inicio
resultado= fibonacci(number)

print ("The number",number,"in fibonacci is:",resultado)
