faturamento = {"SP": 67836.43, 
               "RJ": 36678.66,
               "MG": 29229.88,
               "ES": 27165.48,
               "Outros": 19849.53}
total = 0

for v in faturamento.values():
    total += v

for k, f in faturamento.items():
    print(f'O percentual de {k} no faturamento total é de {(f * 100)/total:.2f}%')
