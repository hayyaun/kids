from math import pi

Q = input('enter your number (1 for arithmetic operations, 2 for area, 3 for volume, 4 for density): ')

if Q == "1":
    operation = input(
        'What mathematical operation do you want to perform? (sum, sub, mul, div): ')
    if operation == "sum":
        x = int(input('Enter a number: '))
        y = int(input('Enter another number: '))
        result = x + y
        print(f'{x} + {y} = {result}')
    elif operation == "sub":
        x = int(input('Enter a number: '))
        y = int(input('Enter another number: '))
        result = x - y
        print(f'{x} - {y} = {result}')
    elif operation == "mul":
        x = int(input('Enter a number: '))
        y = int(input('Enter another number: '))
        result = x * y
        print(f'{x} * {y} = {result}')
    elif operation == "div":
        x = int(input('Enter a number: '))
        y = int(input('Enter another number: '))
        if y != 0:
            result = x / y
            print(f'{x} / {y} = {result}')
        else:
            print('Error: Division by zero.')
    else:
        print('Error: Invalid operation.')


elif Q == "2":
    operation = input(
        'What geometric calculation do you want to perform? (area, mohit): ')
    if operation == "area":
        shape = int(input(
            'Select shape (1 = square, 2 = rectangle, 3 = triangle, 4 = diamond, 5 = circle): '))
        if shape == 1:
            x = int(input('Enter a side length: '))
            area_square = x ** 2
            print('The square area is:', area_square)
        elif shape == 2:
            x = int(input('Enter length: '))
            y = int(input('Enter breadth: '))
            area_rectangle = x * y
            print('The rectangle area is:', area_rectangle)
        elif shape == 3:
            x = int(input('Enter base length: '))
            y = int(input('Enter height: '))
            area_triangle = (x * y) / 2
            print('The triangle area is:', area_triangle)
        elif shape == 4:
            x = int(input('Enter diagonal 1: '))
            y = int(input('Enter diagonal 2: '))
            area_diamond = (x * y) / 2
            print('The diamond area is:', area_diamond)
        elif shape == 5:
            r = int(input('Enter radius: '))
            area_circle = r ** 2 * pi
            print('Circle area is:', area_circle)
        else:
            print('Error: Invalid shape.')

    elif operation == "mohit":
        shape = int(input(
            'Select shape (1 = square, 2 = rectangle, 3 = triangle, 4 = diamond, 5 = circle): '))
        if shape == 1:
            x = int(input('Enter a side length: '))
            mohit_square = x * 4
            print('The square perimeter is:', mohit_square)
        elif shape == 2:
            x = int(input('Enter length: '))
            y = int(input('Enter breadth: '))
            mohit_rectangle = 2 * (x + y)
            print('The rectangle perimeter is:', mohit_rectangle)
        elif shape == 3:
            x = int(input('Enter side 1: '))
            y = int(input('Enter side 2: '))
            z = int(input('Enter side 3: '))
            mohit_triangle = x + y + z
            print('The triangle perimeter is:', mohit_triangle)
        elif shape == 4:
            x = int(input('Enter a side length: '))
            mohit_diamond = x * 4
            print('The diamond perimeter is:', mohit_diamond)
        elif shape == 5:
            r = int(input('Enter radius: '))
            mohit_circle = 2 * r * pi
            print('Circle circumference is:', mohit_circle)
        else:
            print('Error: Invalid shape.')

elif Q == "3":
    operation = input(
        'What volume calculation do you want to perform? (volume): ')
    if operation == "volume":
        shape = int(input(
            'Select shape (1 = cube, 2 = rectangular prism, 3 = pyramid, 4 = sphere): '))
        if shape == 1:
            x = int(input('Enter a side length: '))
            volume = x ** 3
            print('Cube volume is:', volume)
        elif shape == 2:
            x = int(input('Enter length: '))
            y = int(input('Enter breadth: '))
            z = int(input('Enter height: '))
            volume = x * y * z
            print('Rectangular prism volume is:', volume)
        elif shape == 3:
            x = int(input('Enter base length: '))
            y = int(input('Enter height: '))
            volume = (1 / 3) * (x ** 2) * y
            print('Pyramid volume is:', volume)
        elif shape == 4:
            r = int(input('Enter radius: '))
            volume = (4 / 3) * pi * (r ** 3)
            print('Sphere volume is:', volume)
        else:
            print('Error: Invalid shape.')
    else:
        print('Error: Invalid operation.')

elif Q == "4":
    operation = input(
        'What density calculation do you want to perform? (density): ')
    if operation == "density":
        shape = int(input(
            'Select shape (1 = cube, 2 = rectangular prism, 3 = pyramid, 4 = sphere): '))
        # Mass should be provided before volume
        m = int(input('Enter mass (kg): '))
        if shape == 1:
            x = int(input('Enter a side length: '))
            volume = x ** 3
            density = m / volume
            print('Cube density is:', density)
        elif shape == 2:
            x = int(input('Enter length: '))
            y = int(input('Enter breadth: '))
            z = int(input('Enter height: '))
            volume = x * y * z
            density = m / volume
            print('Rectangular prism density is:', density)
        elif shape == 3:
            x = int(input('Enter base length: '))
            y = int(input('Enter height: '))
            volume = (1 / 3) * (x ** 2) * y
            density = m / volume
            print('Pyramid density is:', density)
        elif shape == 4:
            r = int(input('Enter radius: '))
            volume = (4 / 3) * pi * (r ** 3)
            density = m / volume
            print('Sphere density is: ', density)
        else:
            print('Error: Invalid shape.')
    else:
        print('Error: Invalid operation.')

else:
    print('Error: Invalid option.')
