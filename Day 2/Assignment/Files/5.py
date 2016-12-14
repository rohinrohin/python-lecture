file1 = open("5_file1.txt", "r")
file2 = open("5_file2.txt", "r")

same = []
file1only = []
file2only = []

fline1 = file1.readline()
while fline1:
    fline2 = file2.readline()
    if fline1 == fline2:
        same.append(fline1)
    else:
        file1only.append(fline1)
        file2only.append(fline2)
    fline1 = file1.readline()

fline2 = file2.readline()
while fline2:
    file2only.append(fline2)
    fline2 = file2.readline()

print("SAME:", same)
print("FILE 1 ONLY", file1only)
print("FILE 2 ONLY", file2only)

file1.close()
file2.close()