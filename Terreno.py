largura: float
comprimento: float
valorMetro: float
area: float
precoTerreno: float

largura = float(input("Digite a largura do terreno: ").replace(',', '.'))

comprimento = float(input("Digite o comprimento do terreno: ").replace(',', '.'))

valorMetro = float(input("Digite o valor do metro quadrado: ").replace(',', '.'))

area = largura * comprimento
precoTerreno = area * valorMetro

print(f"Area do terreno: = {area:.2f}")
print(f"Preco do terreno:  = {precoTerreno:.2f}")
