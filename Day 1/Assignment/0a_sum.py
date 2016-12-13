# pythonic way
a = input()
print(sum([int(x) for x in list(a)]))

#normal way :)
s = 0
for i in a:
    s += int(i)
print(s)