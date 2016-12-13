wicket = []

while True:
    print("1. Wicket")
    print("2. Game Over")
    print("3. Exit")
    i = input()

    if i=='1':
        run = int(input("partnership run:"))
        wicket.append(run)


    elif i=='2':
        print("Highest partnership: ", max(wicket))
        break

    else:
        break


