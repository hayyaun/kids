
r = 20
r_eye = r/3
space = r/5
r_smile = r - space


def in_circle(x, y, r, center=[0, 0]):
    return (x-center[0])**2 + (y-center[1])**2 < (r-2)**2


for y in range(-r, r):
    for x in range(-r, r):
        if in_circle(x, y, r) \
                and not in_circle(x, y, r_eye, [r_eye+space/4, -space]) \
                and not in_circle(x, y, r_eye, [-r_eye-space/4, -space]) \
                and not (in_circle(x, y, r_smile) and y > space):
            print('⏺', end=' ')
            continue
        print(' ', end=' ')
    print()
