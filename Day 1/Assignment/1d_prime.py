#prime


n = int(input("Enter: "))
l = []


import math
for i in range(n):
    flag = 0
    for j in range(2, math.ceil(math.sqrt(n))):
        if i%j == 0:
            flag = 1
    if not flag:
        l.append(i)


print(l)