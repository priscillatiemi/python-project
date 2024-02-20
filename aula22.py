#Operadores lógicos AND/ OR / NOT / IN E NOT IN 
#Operador lógico AND 

entrada = input('[E]ntrar / [S]air: ')
senha_digitada = input('Digite a senha: ')
senha_correta = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_correta:
    print('Entrando...')
else:
    print('Senha incorreta/ Saindo...')

#Avaliaçao de curto circuito-> a avaliação é curta, pois para no
#primeiro False que encontrar na validação. Não checa mais nada adiante
print(True and False and True)

#Operador Lógico OR -> qualquer valor verdadeiro na condição, fará
#a condição inteira ser verdadeira e vice versa
#Avaliaçao de curto circuito com OR
print(False or False or True)

