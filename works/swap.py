a = 121
b = 225
print(f'before >   a: {a}   b: {b}')

a = a ^ b
b = a ^ b
a = a ^ b
print(f'after  >   a: {a}   b: {b}')
