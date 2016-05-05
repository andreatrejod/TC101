print ("Please give me one number to give you back the factorial:")
x=int(input())
factorial=1

if x >0:
    for a in range (1,x+1):
        factorial=factorial*a
    print ("The factorial of", x, "is: ", factorial)
    factorial=1
