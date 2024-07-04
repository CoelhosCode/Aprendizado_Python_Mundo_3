lista_numeros = list()
contador = 0
while True:
    lista_numeros.append(int(input('Digite um número: ')))
    opçao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    contador += 1
    if opçao == 'N':
        break
print('-=' * 30)
if 5 in lista_numeros:
    print('O número 5 aparece na lista.')
else:
    print('O número 5 não aparece na lista.')
lista_numeros.sort(reverse= True)
print(f'Você diigitou {contador} elementos')
print(f'Os valores em ordem decrescente são {lista_numeros}')