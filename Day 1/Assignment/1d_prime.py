#prime


n = int(input("Enter: "))
l = []


import math
for i in range(n):
    flag = 0
    for j in range(2, math.ceil(math.sqrt(i))):
        if i%j == 0:
            flag = 1
    if not flag:
        l.append(i)


print(l)

#pythonic way using list comprehension
print([i for i in range(2,n) if len([1 for j in range(2,int(math.sqrt(i))+1) if i%j==0])==0])
