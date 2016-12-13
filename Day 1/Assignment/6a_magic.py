n = int(input("Enter n:"))
magicsquare = []
p=[]

for i in range(n):
    p.append(-1)

for j in range(n):
    magicsquare.append(p.copy()) # note the use of copy ~ very important

magicsquare[0][0] = 90
print(magicsquare)

row = 0 #row
col = n // 2 #column

for k in range(1, (n**2) +1):
    print("arr - ", row, col, k) #debuggging
    magicsquare[row][col] = k
    if k%n == 0:
        row += 1
    else:
        if row==0:
            row = n - 1
        else:
            row -= 1
        if col == n-1:
            col = 0
        else:
            col += 1


print(magicsquare)

