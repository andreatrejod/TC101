import os
os.system("clear")

lista=[0,4,2,6,9,8,3,12]
def find_threes(x):
    div = []
    for i in x:
        if i % 3 == 0:
            div.append(i)
            sum = 0
            for i in range(0,len(div)):
                sum = sum + div[i]
    print ("Números divisibles entre 3 de tu lista: ", div)
    print ("Suma de los números divisibles entre 3: ", sum)

find_threes(lista)
