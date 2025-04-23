joao = [250, 300, 200, 150]
pedro = [200, 350, 180, 190]

total_joao = sum(joao)
total_pedro = sum(pedro)

if total_joao > total_pedro:
    print(f"João gastou mais: R$ {total_joao}")
elif total_pedro > total_joao:
    print(f"Pedro gastou mais: R$ {total_pedro}")
else:
    print("João e Pedro gastaram a mesma quantia.")
