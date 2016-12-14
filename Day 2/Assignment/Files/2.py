file1 = open("2_word1.txt", "r")
file2 = open("2_word2.txt", "r")
filew = open("2_write.txt", "w")

arr = []
for i in file1.readlines():
    arr.append(i)
for k in file2.readlines():
    arr.append(k)

arr.sort()
print(arr)

filew.writelines(arr)

file1.close()
file2.close()
filew.close()