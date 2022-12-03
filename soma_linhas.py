m: int
i: int
n: int
j: int
somaLinhas: float = 0

m = int(input("Qual a quantidade de linhas da matriz? "))
while m <= 0 or m > 10:
    m = int(input("Qual a quantidade de linhas da matriz? "))

n = int(input("Qual a quantidade de colunas da matriz? "))
while n <= 0 or n > 10:
    n = int(input("Qual a quantidade de colunas da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    print()
    for j in range(0, n):
        mat[i][j] = float(input(f"Digite os elementos da {i + 1}a linha: ").replace(',', '.'))
print()
print("VETOR GERADO:")
for i in range(0, m):
    if somaLinhas > 0:
        print(f"{somaLinhas}")
        somaLinhas = 0

    for j in range(0, n):
        somaLinhas = somaLinhas + mat[i][j]
