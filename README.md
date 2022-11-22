# Projeto1-Tabuada-Pedro-Hermano
# Tabuada para alunos de matemática do ensino fundamental.

import os

os.system('cls')

from time import sleep


contador = 0
tabuada = input('Qual o número da tabuada?')
tabuada = int(tabuada)
print('Tabuada do', tabuada, 'é:')
while contador < 10:
    contador = contador + 1
    sleep(2)
    print(tabuada, 'x', contador, '=', tabuada * contador)

sleep(2)
print('fim da tabuada de', tabuada)
sleep(2)
print('muito obrigado!')
