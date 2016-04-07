import os
os.system ("clear")

lista=[]
contador2=0
naturals=0
candidate=0
y=1
non=0
regulador=0
lower=int(input("Give the lower bound of numbers to consider "))
upper=int(input("Give the upper bound of numbers to consider: "))
print()
contador=lower

def reverse(num):
  return int(str(num)[::-1])

while(contador<=upper):
    lista.append(contador)
    contador=contador+1

for x in lista:
    z=reverse(lista[contador2])
    if(x==z):
        naturals=naturals+1
    else:
        while(x!=z and regulador<30):
            x=x+z
            z=reverse(x)
            regulador=regulador+1
        if(regulador<30):
            non=non+1
        else:
            candidate=candidate+1
            print("Found Lychrel number: ",lista[contador2],)
        regulador=0
    contador2=contador2+1

print("\nAnd the results for the range",lower,"to",upper,"are: ")
print("Natural palindromes:",naturals)
print("Non Lychrels (become palindrome):",non)
print("Lychrel candidate:",candidate)
