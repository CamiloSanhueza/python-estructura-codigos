import array
import random

filas= input()
columnas= input()

m1 = [[random.randint(0,5)for j in range(columnas)for i in range(filas)]]
m2 = [[random.randint(0,5)for j in range(columnas)for i in range(filas)]]
m3 = [[random.randint(0,5)for j in range(columnas)for i in range(filas)]]
mr = [m1+m2]

suma = [m1[filas][columnas]+m2[filas][columnas]]
resta = [mr-m3]

for i in range(filas):
    for j in range(columnas):
        print(m1[filas][columnas])


        

