import random
import datetime
from colorama import Fore


a = 1
is_first = True
while 1:
    x = random.randint(0, 100)
    c = random.randint(0, x)
    d = random.randint(0, 50)
    e = random.randint(0, 20)
    g = random.randint(0, 70)
    y = random.randint(0, 100)
    time = datetime.datetime.now()
    if is_first == False:
        b = (input(Fore.MAGENTA + "aya mikhahid edame dahid? "))
        if b == "no":
            break
    is_first = False
    n = int(input(Fore.BLUE + "yek adad beyne 0 ta 100 hads bezanin:"))
    if n != x:
        print(Fore.RED+"hads shoma eshtebah bood")
        print(Fore.WHITE+"tarikh:", time)
        print(Fore.CYAN+"tedad hads shoma:", a)
        f = (input(Fore.YELLOW+"aya komak mikhahid?"))
        if f == "yes":
            print(Fore.LIGHTGREEN_EX+"yeki az adad zir gavab hast:")
            komak = [x, e, d, c, g, y]
            random.shuffle(komak)
            print(komak)
            n = int(input(Fore.BLUE+'hads khod ra vared konid: '))
            if n != x:
                print(Fore.RED+"hads shoma eshtebah bood")
    if n == x:
        print(Fore.GREEN+"afarin hadset dorost bood")
        print(Fore.WHITE+"tarikh: ", time)
    a += 1
