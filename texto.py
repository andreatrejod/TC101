import os
os.system ("clear")
print("Let's count some words!!")

textfile = input("What's the name of the document you want me to read?: ")
word = input("What word are you looking for: ").lower()#.lower allow us to 'transform' capital leters into lower

lower_word = word.lower()

def counter(lower_word, textfile):
    contador = 0
    with open(textfile) as openfile:
        for line in openfile:
            line = line.lower()
            contador += line.count(lower_word)
        return(contador)

print("The number of repetitions of" + str(word) + " in text " + str(textfile) + " is: " + str(contador(lower_word, textfile)))
