file1 = open("4_read.txt", "r")
line = file1.readline()
offsets = []
while line:
    offsets.append([line, file1.tell()])
    line = file1.readline()

print(offsets)

file1.seek(0)
for i in offsets[0:len(offsets)-2]:
    a = file1.read(i[1])
    file1.seek(i[1]+1)
    print(a, end="")

file1.close()



