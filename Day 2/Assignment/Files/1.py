file = open("1_words.txt", "r")

unique = {}

for word in file.read().split():
    if word not in unique:
        unique[word] = 1
    else:
        unique[word] += 1

print("Unique words", unique.keys())
print("Occurences", unique)

if input("Type the word to check for occurence: ") in unique:
    print("Word exists.")
else:
    print("Word doesn't exist")


file.close()