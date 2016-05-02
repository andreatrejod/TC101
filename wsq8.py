print("On To Functions")
print("Este programa te ayuda a hacer la suma resta multiplicación división y residuo de 2 números \n")
def suma (numero1,numero2):
    resultsuma=numero1+numero2
    print("La suma de", numero1,"+",numero2,"es:",resultsuma)
    return resultsuma
s=suma(4,4)

def resta (numero1,numero2):
    resultresta=numero1-numero2
    print("La resta de", numero1,"-",numero2,"es:",resultresta)
    return resultresta
r=resta(5,4)

def multiplicacion (numero1,numero2):
    resultmultiplicacion=numero1*numero2
    print("La multiplicacion de", numero1,"X",numero2,"es:",resultmultiplicacion)
    return resultmultiplicacion
m=multiplicacion(5,4)

def division (numero1,numero2):
    resultdivision=numero1//numero2
    print("La division de", numero1,"/",numero2,"es:",resultdivision)
    return resultdivision
d=division(20,4)

def residuo (numero1,numero2):
    resultresiduo=numero1%numero2
    print("El residuo de", numero1,"%",numero2,"es:",resultresiduo)
    return resultresiduo
resi=residuo(20,3)
