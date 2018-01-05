import pprint
key_list = ['a', 'b', 'c']
d = {}
for value, key in enumerate(key_list):
    d[key] = list(range((value*10)+1, (value*10)+11))
pprint.pprint(d)