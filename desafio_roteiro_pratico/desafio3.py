gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print("João gastou mais dinheiro ao longo do mês.")
elif total_pedro > total_joao:
    print("Pedro gastou mais dinheiro ao longo do mês.")
else:
    print("João e Pedro gastaram a mesma quantidade de dinheiro ao longo do mês.")