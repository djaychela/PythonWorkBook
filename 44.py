from string import ascii_lowercase
from itertools import zip_longest

# with open('ex_44.txt','w') as file:
#     for i in range(0, len(ascii_lowercase), 3):
#         file.write(ascii_lowercase[i:i+3]+'\n')

triples = zip_longest(ascii_lowercase[::3], ascii_lowercase[1::3], ascii_lowercase[2::3])
print(*triples)
