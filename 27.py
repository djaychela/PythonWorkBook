def acceleration(v1,v2,t1,t2):
    return (v2-v1)/(t2-t1)

v1 = int(input('V1: '))
v2 = int(input('V2: '))
t1 = int(input('T1: '))
t2 = int(input('T2: '))
print(acceleration(v1,v2,t1,t2))