

import statistics  # Este módulo permite calcular operaciones estadísticas como las que necesitamos en este programa.

lista = [float(input("Please give me the first number: ")), float(input("Please give me the second number: ")),
float(input("Please give me the third number: ")), float(input("Please give me the fourth number: ")),
float(input("Please give me the fifth number: ")),float(input("Please give me the sixth number: ")),
float(input("Please give me the seventh number: ")),float(input("Please give me the eighth number: ")),
float(input("Please give me the nineth number: ")),float(input("Please give me the tenth number: "))]



promedio = statistics.mean(lista) #esta función permite encontrar el promedio
print("The average of your numbers is: {}".format(promedio))
suma = sum(lista)
print("The sum de of the numbers given by you is:{} ".format(suma))
std_des = statistics.stdev(lista)#esta función permite encontrar la desviación standard
print("The standard deviation of your numbers is: {}".format(std_des))
