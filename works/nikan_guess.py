import random

javab = random.randint(1, 99)
name = input('what is your name? ')
hads = int(input(f'so {name} what is your hads? '))

while hads != javab:
    if hads > javab:
        print('mine is smoller')
    else:
        print('mine is larger')
    hads = int(input('what is your hads? '))
print('ooooooooh myyy god.', name, 'you are very very smart.', name, 'e bahoosh')
