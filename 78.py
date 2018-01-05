from string import printable
import random

password = ''
for i in range(6):
    password += printable[random.randint(0,len(printable)-1)]

print(password)

chosen = random.sample(printable, 6)
password2 = ''.join(chosen)
print(password2)