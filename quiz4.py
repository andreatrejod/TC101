import os
os.system ("clear")
import math
print("Euler Number")
stop=int(input("Please give me the number of the end of the sequency: "))

def euler_calc (stop):
    counter=0
    other=0
    while(counter<=stop):
        f=math.factorial(counter)
        other=other+1/f
        counter=counter+1

    return other
result=euler_calc(stop)
print(result)
