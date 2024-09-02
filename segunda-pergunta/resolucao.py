def verificador_de_fibonacci(numero):
    fibonacci = fibonacci_anterior = 0
    soma = 1
    while True:
        if numero > fibonacci:
            fibonacci_anterior = fibonacci
            fibonacci += soma
            soma = fibonacci_anterior
        elif numero < fibonacci:
            return False
        else:
            return True


# Programa Principal
while True:
    try:
        numero = int(input('Digite um número e eu te direi se faz parte da Sequência de Fibonacci: '))
    except ValueError:
        print('Erro, você não digitou um número.')
    else:
        break

if verificador_de_fibonacci(numero):
    print('É um número da Sequência de Fibonacci!')
else:
    print('Não é um número da Sequência de Fibonacci!')
    