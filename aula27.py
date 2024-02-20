#Métodos com string
mensagem = 'Adoro comida japonesa'

existe = input('Qual letra quer encontrar? ')
letra = mensagem.find(existe)
#print(mensagem.find('Adoro'))

if letra:
    print(f'A letra {existe} está na mensagem.')
else:
    print('Essa letra nao existe na mensagem')