emplist = \
    [
            ['123', 'Rohin', 9000, 1090, 1200], #EMPID, NAME, BASIC, DA, HRA
            ['124', 'Ram', 9000, 1080, 1300],
            ['125', 'Shyam', 9000, 1090, 1400]
    ]

empdict = {}

for i in emplist:
    empdict[i[0]] = sum(i[2:]) #slicing

print(empdict)

