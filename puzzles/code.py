def fibonacci(n: int):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return 1


for i in range(5):
    print(f'{fibonacci(i)}', end=' ')