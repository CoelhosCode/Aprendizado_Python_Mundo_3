tupla = ()
numeros_pares = []
for numeros in range(4):
    numeros_escolhidos = int(input('Digite um número: '))
    tupla = tupla + (numeros_escolhidos,)
    if numeros_escolhidos % 2 == 0:
        numeros_pares.append(numeros_escolhidos)
repeticao_9 = tupla.count(9)
print(f'O número 9, aparece {repeticao_9} vezes')
if 3 in tupla:
    posicao = tupla.index(3) + 1
    print(f'O número 3 apareceu na posição {posicao}°')
else:
    print('O número 3, não apareceu nesta seleção.')
print(f'Você digitou os valores: {tupla}')
print(f'Os número pares digitados foram: {numeros_pares}')