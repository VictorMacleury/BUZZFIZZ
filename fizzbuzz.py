'''
Jogo do Fizzbuzz, 
se o número for dividio por 3, Printar FIZZ
Se o número for dividido por 5, printar BUZZ
Se o número for dividido por 3 e 5, printar FIZZBUZZ
'''

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        print(f'FIZZBUZZ! O {n} é divisível por 3 e 5!')
    if n % 5 == 0:
        print(f'BUZZ! O {n} é divisível por 5!')
    if n % 3 == 0:
        print(f'FIZZ! O {n} é divisível por 3!')
    return n

from random import randint

for i in range(100):
    aleadorio = randint(0,100)

    print(fb(aleadorio))

