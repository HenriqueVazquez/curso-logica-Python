preco: float
dinheiro: float
troco: float
resto: float
quantidade: int

preco = float(input("Preco unitario do produto: ").replace(',', '.'))

quantidade = int(input("Quantidade comprada: "))

dinheiro = float(input("Dinheiro recebido: ").replace(',', '.'))

if dinheiro >= (preco * quantidade):
    troco = float(dinheiro - preco * quantidade)
    print(f"TROCO = {troco:.2f}")

else:
    resto = preco * quantidade - dinheiro
    print(f"DINHEIRO INSUFICIENTE. FALTAM {resto:.2f} REAIS")
