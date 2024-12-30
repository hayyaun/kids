# 70% code by Nikan
# 30% code by GPT-4o mini

def save_username(user_name):
    with open("usernames.txt", "a") as file:
        file.write(user_name + "\n")

user_name = input('please enter your real name: ')
if user_name not in ['Noyan', 'Hayyaun', 'Haman', 'Nikan', 'Mobin', 'Mahdi', 'Barbod']:
    print("oh sorry you can't enter our site!")
    save_username(user_name)
else:
    save_username(user_name)
    
    n1 = 2
    n2 = 2
    m = n1 + n2
    print('2', '+', '2', '=', m)

    secure_1 = input('please enter 1: ')
    if secure_1 == '1':
        continue_1 = input('do you like to continue our program? (yes/no) ')
        if continue_1.lower() == 'yes':
            brother_sister = input("do you have any brother and sister? (1- yes I have one or more brother 2- yes I have one or more sister 3- No I haven't any brother and sister) ")
            print("OK goodby!")
        else:
            print("OK goodby!")
    else:
        print("you are a bad boy. bi tarbiat!")