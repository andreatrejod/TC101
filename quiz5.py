import os
os.system ("clear")

word=(str.lower(input("Please write the word you want to consult: ")))
def palindrome(num):
    return str(num)[::-1]

result=palindrome(word)

if (result==word):
    print("Yes! the word is a palindrome")

else:
    print("Oh oh, sorry, this word is not a palindrome")
