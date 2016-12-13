a = int(input("Enter a number"))
b = int(input("Enter a number"))
hcf = 1

maxi = a
if b > maxi:
    maxi = b

for i in range(1, maxi + 1):
    if a%i == 0 and b%i == 0:
        hcf = i

print(hcf)
