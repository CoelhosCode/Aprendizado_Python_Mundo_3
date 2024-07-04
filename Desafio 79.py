lista_numeros = list()
while True:
    numeros = int(input('Digite um valor: '))
    if numeros in lista_numeros:
        print('Valor duplicado! Não irei adicionar...')
    else:
        lista_numeros.append(numeros)
        print('Número adicionado com sucesso...')
        opçao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opçao == 'N':
        break
lista_numeros.sort()
print(f'Você digitou os valores {lista_numeros}')