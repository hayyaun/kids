# Show Primary numbers below n
# 1. Get a number from user in Terminal
# 2. Print each primary number below n

# Complete this code:

# TODO get the number n from user

i = 2
while i < n:
    is_primary = True  # flag
    j = 2
    while j < i:
        if i % j == 0:
            # TODO set is primary False
            break  # stop the loop
        # TODO increment j

    # TODO print number if primary
    # TODO increment i
