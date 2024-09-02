import json

def menor_valor_de_faturamento(dados):
    menor_numero = None

    for v in dados.values():
        if v == None:
            pass
        elif menor_numero == None:
            menor_numero = v
        elif v < menor_numero:
            menor_numero = v

    return menor_numero


def maior_valor_de_faturamento(dados):
    maior_numero = None

    for v in dados.values():
        if v == None:
            pass
        elif maior_numero == None:
            maior_numero = v
        elif v > maior_numero:
            maior_numero = v

    return maior_numero


def dias_com_valores_superiores(dados):
    total = dias = dias_superior = 0

    for v in dados.values():
        if v != None:
            total += v
            dias += 1
    
    media = total / dias

    for n in dados.values():
        if n == None:
            pass
        elif n > media:
            dias_superior += 1

    return dias_superior


# Programa Principal
with open('vetor.json', 'r') as file:
    dados_faturamento = json.load(file)

print(
    f'O menor valor de faturamento ocorrido em um dia do mês: {menor_valor_de_faturamento(dados_faturamento["daily_revenue"])}\n'
    f'O maior valor de faturamento ocorrido em um dia do mês foi: {maior_valor_de_faturamento(dados_faturamento["daily_revenue"])}\n'
    f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi: {dias_com_valores_superiores(dados_faturamento["daily_revenue"])}'
)
