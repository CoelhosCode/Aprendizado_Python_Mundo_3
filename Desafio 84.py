dados_pessoas = list()
nome_e_peso = list()
contador = 0
maior_peso = menor_peso = 0
while True:
    nome_e_peso.append(str(input('Nome: ')))
    nome_e_peso.append(float(input('Peso: ')))
    if len(dados_pessoas) == 0:
        maior_peso = menor_peso = nome_e_peso[1]
    else:
        if nome_e_peso[1] > maior_peso:
            maior_peso = nome_e_peso[1]
        if nome_e_peso[1] < menor_peso:
            menor_peso = nome_e_peso[1]
    opçao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    dados_pessoas.append(nome_e_peso[:])
    nome_e_peso.clear()
    contador += 1
    if opçao == 'N':
        break
print('-=' * 30)
print(f'Foram cadastrados {contador} pessoas.')
print(f'O maior peso foi de {maior_peso}. Peso de ', end='')
for pessoa in dados_pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso foi de {menor_peso}. Peso de ', end='')
for pessoa in dados_pessoas:        
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end='')
print()