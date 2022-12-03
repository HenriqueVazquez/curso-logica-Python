import math

raio: float
area: float
pi = 3.14159

print("Area de um criculo:")
raio = float(input("Informe o raio: ").replace(',', '.'))

area = pi * math.pow(raio, 2)

print(f"Area =  {area:.3f} ")
