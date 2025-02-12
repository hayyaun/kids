import random
from colorama import Back, Style, Fore

# variables & lists
name = '...'
star = ["💫", "💫", "💫"]
items1 = ["💔", "👋", "7"]
items2 = ["💔", "7", "👋", "7"]
items3 = ["💔", "7", "7", "👋", "7", "💣"]

# check name
like = str(input('Do you like cheat (yes or no)? '))
if like == 'yes':
    name = str(input("What's your name(last name or frist name)? "))
    print(name, 'have good game!')
elif like == 'no':
    for i in range(100):
        star.append('💫')

if name == 'hami':
    items3.remove('💣')
    print('Hello teacher!')
    print('How are you today?')
    like = str(input('you like stars (yes or no)?'))
    if like == 'yes':
        for i in range(100):
            star.append('💫')
    print('ok')

if name == 'barbod':
    items3.append("❌")
    items1.append("❌")
    items2.append('❌')
    print('is ok!')

if name == 'haman':
    items1.remove("💔")
    items2.remove('💔')
    items3.remove('💣')
    items3.remove('💔')
    items3.append("💯")
    print('is ok')

if name == 'saketbash':
    for i in range(20):
        star.append('💫')

if name == 'dalirsefat':
    print('hello barbod')
    print('barbod!')
    print('this is lose code!')
    star.clear()
    star.append('💫')
    like3 = str(input('you like ...(yes or no)? '))
    if like3 == 'yes':
        while True:
            print('😈😈😈')

if name == 'abbas':
    print('hello abbas')
    print('saketbash!')
    print('this is lose code!')
    star.clear()
    star.append('💫')
    like = str(input('you like ...(yes or no)? '))
    if like == 'yes':
        while True:
            print('😈😈😈')

# game loop
while True:
    r = str(input("What to do? (roll/stars/exit) \n> "))
    s = len(star)

    # roll dice
    if r == "roll":
        x1 = random.choice(items1)
        x2 = random.choice(items2)
        x3 = random.choice(items3)

        print(Fore.BLACK + Back.BLUE + x1 + x2 + x3 + Style.RESET_ALL)

        if x3 == "💣":  # lose
            print(Fore.RED + Back.WHITE + "BOOOOOOM! 💣" + Style.RESET_ALL)
            star.clear()
            star.append('💫')
        if x1 == x2 == x3 == "7":  # score +1
            star.append("💫")
            print(Fore.YELLOW + Back.WHITE + "You win!" + Style.RESET_ALL)
        if x1 == x2 == x3 == "💔":  # score -1
            star.pop()
            print(Fore.RED + Back.WHITE + "You lose!" + Style.RESET_ALL)
        if x1 == x2 == x3 == '❌':
            for k in range(1000):
                star.append('💫')  # score +1000

    # cheat code - list
    if r == "im ali!":
        print("HELLO ALI! \nHOW ARE YOU TODAY?")
        items1.remove("💔")
        items2.remove('💔')
        items3.remove('💣')
        items3.remove('💔')
        items3.append("💯")
        items3.append("❌")
        items1.append("❌")
        items2.append('❌')
        print("EZAY")

    # cheat code - 10 stars
    if r == 'ali':
        for i in range(10):
            star.append("💫")

    # lose code - 5 stars
    if r == "mohammad":
        for i in range(5):
            if len(star):
                star.pop()

    # stars
    if r == "stars":
        print(Fore.YELLOW + Back.WHITE + f'Stars = {s}💫' + Style.RESET_ALL)

    # terminate game
    if r == "exit":
        print("Goodbye!", s)
        break
