statedict = {
    ('Karnataka', 'Bangalore'): ['PES Uni', 'PES South']
} #sample starter dict

while True:
    print(statedict)
    print("1. Add key")
    print("2. Modify key")
    print("3. Remove key")
    print("4. Print Dict")
    inp = int(input("Enter: "))

    if inp == 1:
        statecit = tuple(input("Enter state <space> city").split(" "))
        places = input("Enter places of interest with spaces: ").split(" ")
        print(places)
        statedict[statecit] = places

    if inp == 2:
        statecit = tuple(input("Enter state <space> city to find: ").split(" "))
        if statecit in statedict:
            print(statedict[statecit])
            statedict[statecit] = input("Enter modification with spaces: ").split(" ")
        else:
            print("not found. ")

    if inp == 3:
        statecit = tuple(input("Enter state <space> city to remove: ").split(" "))
        if statecit in statedict:
            statedict.pop(statecit)
            print("removed. ")
        else:
            print("not found. ")

    if inp == 4:
        print(statedict)







