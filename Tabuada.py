

contador = 0
tabuada = input('Qual o número da tabuada?')
tabuada = int(tabuada)
print('Tabuada do', tabuada, 'é:')
while contador < 10:
    contador = contador + 1
    print(tabuada, 'x', contador, '=', tabuada * contador)

print('fim da tabuada de', tabuada)
print('muito obrigado!')
