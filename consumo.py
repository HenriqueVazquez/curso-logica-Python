distancia: float
combustivelGasto: float
consumo: float

print("Calculo de consumo")
print()
distancia = float(input("Distancia percorrida: ").replace(',', '.'))
combustivelGasto = float(input("Combustível gasto: ").replace(',', '.'))

consumo = distancia / combustivelGasto

print(f"O consumo medio = {consumo:.3f} ")
