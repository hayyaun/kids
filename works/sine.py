import math
import os
import time

t_size = os.get_terminal_size()
l = int(t_size.columns / 2)
a = int(min(t_size.lines / 2, l / 6))
freq = 1/(l/(6*math.pi))


x = 0
while True:
    time.sleep(0.07)
    os.system('clear')
    for screen_y in range(-a, a):  # lines
        for screen_x in range(l):  # columns
            y = (a*2/3) * math.sin((screen_x - x)*freq)
            if abs(screen_y - y) < 0.5:
                print('⏺', end=' ')
            else:
                print(' ', end=' ')
        print()
    x -= 1
