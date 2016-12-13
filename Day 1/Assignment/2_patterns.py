#patterns

count = 0
inp = int(input("enter"))
for i in range(0, inp):

    for j in range(0, inp):
        if i==count:
            print(1, end=" ")
        else:
            print(0, end=" ")
        count += 1
    count = 0
    print()

print()

suma = 0
for i in range(1, inp+1):
    suma += i
    if inp==i:
        print(str(i), end=" ")
        print("=", suma, end=" ")
    else:
        print(str(i) + " +", end=" ")

print()

suma = 0
for j in range(1, inp+2):
    suma = 0
    for i in range(1, j):
        suma += i
        if i==j-1:
            print(str(i), end=" ")
            print("=", suma, end=" ")
        else:
            print(str(i) + " +", end=" ")
    print()


suma = 0
for j in range(1, inp+2):
    suma = 0
    print(" "*inp*(inp-j+1), end="")
    for i in range(1, j):
        suma += i
        if i==j-1:
            print(str(i), end=" ")
            print("=", suma, end=" ")
        else:
            print(str(i) + " +", end=" ")
    print()

