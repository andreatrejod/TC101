import os
os.system ("clear")

num_list1=int(input("Please give me the numbers of your first list: "))
num_list2=int(input("Please give me the numbers of your first list: "))
list1=[]
list2=[]
vector=[]
for n in range(num_list1):
    num=int(input("Please give me the number of the list 1: "))
    list1.append(num)

for n in range(num_list2):
    num2=int(input("Please give me the number of the list 2: "))
    list2.append(num2)

def dot_product():
    if len(list1)==len(list2):
        for n in range(num_list1):
            vector.append(list1[n]*list2[n])
            result=sum(vector)
        return result
    else:
        return float("NaN")

print("The product of the point is: ", list1, " and ", list2, " is: ", dot_product())
