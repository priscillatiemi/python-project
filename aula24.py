#Operadores In e Not In
# String são iteráveis -> pode navegar item por item
nome = 'Priscilla'
encontrar = input('Digite a letra que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao existe em {nome}')
print('á' not in nome)
print(10*'-')
print('a' not in nome)