d = {"a": 1, "b": 2, "c": 3}
e = {}
for key in d.keys():
    if d[key]<=1:
        e[key]=d[key]
print(e)