
#Task-2 Simple Password Genrator

import random
import string

length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity (strong/medium/weak): ")

if complexity == 'strong':
    chars = string.ascii_letters + string.digits + string.punctuation
elif complexity == 'medium':
    chars = string.ascii_letters + string.digits
else:
    chars = string.ascii_letters

password = ""

for z in range(length):
    password += random.choice(chars)


password = ''.join([random.choice(chars) for z in range(length)])

print("Your random password is:", password)