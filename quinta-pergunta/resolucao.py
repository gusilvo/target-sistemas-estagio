def inverter_string(string):
    string_invertida = []
    for l in range(len(string) - 1, -1, -1):
        string_invertida.append(string[l])

    return ''.join(string_invertida)


# Programa Principal
string = 'Target Sistemas'
string_invertida = inverter_string(string)

print(string_invertida)
