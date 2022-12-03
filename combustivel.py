Gasolina: int = 0
Alcool: int = 0
Diesel: int = 0
codigo: int = 0

while codigo != 4:
    codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

    while codigo < 1 or codigo > 4:
        codigo = int(input("Informe um codigo valido (1, 2, 3) ou 4 para parar: "))
        match codigo:
            case 1:
                Alcool = Alcool + 1
            case 2:
                Gasolina = Gasolina + 1
            case 3:
                Diesel = Diesel + 1

print("MUITO OBRIGADO")
print(f"1- Alcool: {Alcool}")
print(f"2- Gasolina: {Gasolina}")
print(f"3- Diesel: {Diesel}")
