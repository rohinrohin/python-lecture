file = open("6_read.txt", "r")
bufffile = open("6_read.txt", "r")

for i in file.readlines():
    if i[:6] == "AUTHOR":
        bufffile = open("6_"+ i.split()[1], "w")
    bufffile.writelines(i)

file.close()
bufffile.close()