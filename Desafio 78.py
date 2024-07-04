valores = list()
maior_valor = 0
menor_valor = 0
for numeros in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicao {numeros}: ')))
    if numeros == 0:
        maior_valor = menor_valor = valores[numeros]
    else:
        if valores[numeros] > maior_valor:
            maior_valor = valores[numeros]
        if valores[numeros] < menor_valor:
            menor_valor = valores[numeros]
print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor é o {maior_valor} e encontra-se nas posições', end=' ')
for indice, valor in enumerate(valores):
    if valor == maior_valor:
        print(f'{indice}', end= ' ')
print()
print(f'O menor valor é {menor_valor} e encontra-se nas posições', end=' ')
for indice, valor in enumerate(valores):
    if valor == menor_valor:
        print(f'{indice}', end=' ')