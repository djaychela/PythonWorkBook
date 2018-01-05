d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key in d.keys():
    print(f"{key} has value {d[key]}")