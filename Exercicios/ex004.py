# Ler algo na tela e responder qual o tipo primitivo e se é numérico ou é do alfabeto.
algo = input('Digite algo: ')
print('O tipo primitivo do que foi digitado é: ',type(algo))
print('O que foi digitado é somente espaços: ',algo.isspace())
print('O que foi digitado, é numérico: ',algo.isnumeric())
print('O que foi digitado, é do alfabeto: ',algo.isalpha())
print('O que foi digitado é alphanumérico: ',algo.isalnum())
print('O que foi digitado é decimal: ',algo.isdecimal())
print('O que foi digitado está tudo em letras minusculas: ',algo.islower())
print('O que foi digitado está tudo em letras maiusculas: ',algo.isupper())
print('o que foi digitalizado está capitalizado: ',algo.istitle())