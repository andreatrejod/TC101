def gcd (x,y):
    if(x==y):
        return x
    elif (x>y):
        return gcd(x-y,y)
    else:
        return gcd (x,y-x)

number1=int(input("Give me the first number please: "))
number2=int(input("Give me the second number please: "))
result=gcd(number1,number2)



print("The gratest common denominator is: ",result)
