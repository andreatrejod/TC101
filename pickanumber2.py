import random

a = random.randint (1,100)
b=0
c=0
while a!= b:
    b = int(input("Pick a number between 1 and 100: "))
    if b != a:
        if a > b:
            print ("Noupe, this number is too low, try again")
            c += 1

        else:
            print ("Noupe, this number is too high, try again")
            c += 1

    else:
        print ("Great! you just got lucky, kidding, YOU WON!")
        c += 1
        print ("attemps:",c)
