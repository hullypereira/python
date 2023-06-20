gastos = []  # Lista para armazenar os gastos mensais

# Loop para inserir os gastos
while True:
    gasto = input("Digite o valor gasto (ou 'sair' para encerrar): ")
    if gasto.lower() == "sair":
        break
    try:
        gasto = float(gasto)
        gastos.append(gasto)
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido.")

# Cálculo do total gasto
total_gasto = sum(gastos)

# Exibição do total gasto
print("Total gasto no mês: R$", total_gasto)
