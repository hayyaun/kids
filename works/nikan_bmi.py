# code by Nikan Nejatifar
# BMI test


b = int(input('Enter your height (cm) : '))
b = b / 100
c = int(input('Enter your weight (kg) : '))
a = c/b**2
print('your BMI is: ', round(a, 2))

pre = 'Your status is'
if a <= 18.4:
    print(pre, 'Underweight')
elif 18.4 < a <= 24.9:
    print(pre, 'Normal')
elif 24.9 < a <= 39.9:
    print(pre, 'Overweight')
else:
    print(pre, 'Obese')
