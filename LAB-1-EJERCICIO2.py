
import random

filas= 2
columnas= 2

m1 = [[random.randint(0,10)for j in range(columnas)for i in range(filas)]]

for i in range(filas):
    for j in range(columnas):
        print(m1[filas][columnas])
    

        