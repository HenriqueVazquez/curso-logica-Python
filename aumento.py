salario: float
salarioAtualizado: float
aumento: float
porcentagem: float

print("Calcular ajuste do funcionario")
print()

salario = float(input("Digite o salrio do funcionario: ").replace(',', '.'))

if salario <= 1000:
    porcentagem = 0.20
elif salario <= 3000:
    porcentagem = 0.15

elif salario <= 8000:
    porcentagem = 0.10
else:
    print("Calcule novamente")

aumento = salario * porcentagem
salarioAtualizado = salario + aumento

print(f"Novo salario = {salarioAtualizado:.2f}")
print(f"Aumento = {aumento:.2f}")
print(f"Porcentagem = {porcentagem * 100:.0f}%")
