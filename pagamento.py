nome: str
valorHora: float
pagamento: float
horasTrabalhadas: int

nome = input("Nome: ")
valorHora = float(input("Valor por hora: ").replace(',', '.'))

horasTrabalhadas = int(input("Horas trabalhadas: "))

pagamento = float(valorHora * horasTrabalhadas)

print(f"O pagamento para {nome} deve ser R${pagamento:.2f}")
