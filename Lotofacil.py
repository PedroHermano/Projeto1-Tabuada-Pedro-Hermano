from random import randint
numeros = (randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25), randint(1, 25))
print(f'os valores sorteados foram: ', end = " ")
for n in numeros:
    print(f'{n}', end = " ")
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

print(sorted(numeros))
