import platform

import requests

print('Hello. You can use our program')
name = (input("what's your name? "))
classno = float(input("what's your class?(7.1, 7.2, 7.3, 7.4) "))
height = int(input("please enter your height? "))
weight = int(input("please enter your weight? "))
favorite_sport = input("what's your favorite sport? ")
operating_system = platform.system()
machine_name = platform.node()
print('thank you for using this program')


url = 'http://hayyaun.ir/api/nikan'
data = {
    'name': name,
    'class': classno,
    'height': height,
    'weight': weight,
    'fav_sport': favorite_sport,
    'os': operating_system,
    'machine': machine_name
}

response = requests.post(url, json=data)
