# Check if a number is prime number
# 1. Get a number from user in Terminal
# 2. Loop to see if it divides by any number

# Complete this code:

n = int(input('Enter a number: '))

is_prime = True

for i in range(2, n):
  # Check if n is divided by i
  # if Yes: set is_prime False
  # and stop the loop
  # if No: do nothing...

if is_prime:
    print(n, 'is prime')
else:
    print(n, 'is not prime')
