#combinatorial method of pascals

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(0))

l = []
def ncr(n, r):
    return fact(n)/(fact(n-r)*fact(r))


for i in range(int(input("Enter: "))):
    p = []
    for j in range(0, i+1):
        p.append(int(ncr(i, j)))
    l.append(p)


print(l)

