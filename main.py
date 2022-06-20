import string
import random

list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)
character_number = input('please enter how many digits you want in your password: ')
while True:
    try:
        character_number = int(character_number)
        if character_number < 6:
            print('The password needs to be more than 5 digits')
            character_number = input('please enter the number again: ')
        else:
            break
    except ValueError:
        print('please enter a valid number')
        character_number = input('please enter how many digits you want in your password: ')

random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

password = []

for i in range(part1):
    password.append(list1[i])
    password.append(list4[i])
for i in range(part2):
    password.append(list3[i])
    password.append(list2[i])

password = "".join(password[0:])
print(password)




