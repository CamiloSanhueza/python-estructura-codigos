import numpy as np

# Las 3 matrices deben ser generadas de forma aleatoria
# Se genera la primera matriz aleatoria de números del 1 al 10
matrix_a = np.random.randint(1, 11, size=(3, 3))

# Se genera la segunda matriz aleatoria de números del 11 al 30
matrix_b = np.random.randint(11, 31, size=(3, 3))

# Se genera la tercera matriz aleatoria de números del -1 al -10
matrix_c = np.random.randint(-10, 0, size=(3, 3))

# Se muestran las matrices generadas
print("Matriz A:")
print(matrix_a)
print("\nMatriz B:")
print(matrix_b)
print("\nMatriz C:")
print(matrix_c)

# Se calcula el producto de matrices (A + B) · C
result_left = np.dot(matrix_a + matrix_b, matrix_c)

# Se calcula el producto de matrices A · C y B · C
result_right = np.dot(matrix_a, matrix_c) + np.dot(matrix_b, matrix_c)

# Se verifica si se cumple la propiedad (A + B) · C = A · C + B · C
if np.array_equal(result_left, result_right):
    print("\nLa propiedad (A + B) · C = A · C + B · C se cumple.")
else:
    print("\nLa propiedad (A + B) · C = A · C + B · C no se cumple.")
