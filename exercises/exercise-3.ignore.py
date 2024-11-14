# Show Primary numbers below n
# 1. Get a number from user in Terminal
# 2. Print each primary number below n

# Complete this code:

n = int(input('Enter a number: '))
i = 2

while i < n:
    is_primary = True
    j = 2
    while j < i:
        if i % j == 0:
            is_primary = False
            break
        j += 1
    if is_primary:
        print(i, 'is primary')
    i += 1
