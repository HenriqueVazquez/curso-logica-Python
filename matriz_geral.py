import math

i: int = 0
n: int = 0
j: int = 0
linhaEscolhida: int = 0
colunaEscolhida: int = 0
somaPositivos: float = 0

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: ").replace(',', '.'))

print()

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] >= 0:
            somaPositivos = somaPositivos + mat[i][j]

print(f"SOMA DOS POSITIVOS: {somaPositivos:.1f}")
print()

linhaEscolhida = int(input("Escolha uma linha: "))

print(f"LINHA ESCOLHIDA: ", end="")

for i in range(0, n):
    print(f"{mat[linhaEscolhida][i]:.1f} ", end="")
print()
print()

colunaEscolhida = int(input("Escolha uma coluna: "))

print(f"COLUNA ESCOLHIDA: ", end="")

for i in range(0, n):
    print(f"{mat[i][colunaEscolhida]:.1f} ", end="")

print()
print()
print()

print("DIAGONAL PRINCIPAL: ", end="")
for i in range(0, n):
    print(f"{mat[i][i]:.1f} ", end="")

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            mat[i][j] = math.pow(mat[i][j], 2)
print()
print()
print("MATRIZ ALTERADA: ")

for i in range(0, n):
    for j in range(0, n):
        print(f"{mat[i][j]:.1f} ", end="")
    print()
