import platform

print('Thank you for use our program')
name = (input("what's your name? "))
classs = float(input("what's your class?(7.1, 7.2, 7.3, 7.4) "))
height = int(input("please enter your height? "))
weight = int(input("please enter your weight? "))
favotite_sport = (input("what's your favorite sport? "))

Platform = ('Platform:', platform.platform())
Architecture = ('Architecture:', platform.architecture())
Operating_system = ('Operating system:', platform.system())
Machine_name = ('Machine name:', platform.node())
python_version = ('Python version:', platform.python_version())

with open('names.txt', 'a') as f:
    f.write(f'{name}, {classs}, {height}, {weight}, {favotite_sport}, {Platform}, {
            Operating_system}, {Machine_name}, {Architecture}, {python_version} \n')
print('thank you for use this program')
