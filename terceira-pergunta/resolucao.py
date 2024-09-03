import json

def menor_valor_de_faturamento(dados):
    menor_numero = None

    for d in dados:
        if d['valor'] == 0:
            pass
        elif menor_numero == None:
            menor_numero = d['valor']
        elif d['valor'] < menor_numero:
            menor_numero = d['valor']

    return menor_numero


def maior_valor_de_faturamento(dados):
    maior_numero = None

    for d in dados:
        if d['valor'] == 0:
            pass
        elif maior_numero == None:
            maior_numero = d['valor']
        elif d['valor'] > maior_numero:
            maior_numero = d['valor']

    return maior_numero


def dias_com_valores_superiores(dados):
    total = dias = dias_superior = 0

    for d in dados:
        if d['valor'] != 0:
            total += d['valor']
            dias += 1
    
    media = total / dias

    for n in dados:
        if n['valor'] == 0:
            pass
        elif n['valor'] > media:
            dias_superior += 1

    return dias_superior


# Programa Principal
with open('dados.json', 'r') as file:
    dados_faturamento = json.load(file)

print(
    f'O menor valor de faturamento ocorrido em um dia do mês foi {menor_valor_de_faturamento(dados_faturamento)}\n'
    f'O maior valor de faturamento ocorrido em um dia do mês foi {maior_valor_de_faturamento(dados_faturamento)}\n'
    f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi de {dias_com_valores_superiores(dados_faturamento)}'
)
