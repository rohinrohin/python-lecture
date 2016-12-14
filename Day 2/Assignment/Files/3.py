file1 = open("3_empfile.txt", "r")
empdict = {}

for x in (file1.readlines()):
    (empname, empdept) = str(x).split()
    if empdept not in empdict:
        empdict[empdept] = []

    empdict[empdept].append(empname)

print("String: ")
for i in empdict:
    print(i, ": ", ", ".join(empdict[i]))

print("List: ")
print(empdict)