i: int
n: int = 0
j: int
somaNegativos: int = 0

n = int(input("Qual a ordem da matriz? "))

while n <= 0 or n > 10:
    n = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")
for i in range(0, n):
    print(f"{mat[i][i]} ", end="")

print()

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            somaNegativos = somaNegativos + 1

print(f"QUANTIDADE DE NEGATIVOS = {somaNegativos}")
