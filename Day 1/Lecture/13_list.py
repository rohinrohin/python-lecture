# list
#	has # of elements
#	elements can be heterogeneous
#	indexed by int
#	create :  []
# 	index : always []
#	size : dynamic
a = [11, 22, 33, 44]
print(a, len(a))
# index:
# count from 0
print(a[2])
# checks for index out of bounds error
#print(a[5])
#a[4] = 55
#
a.append(55)
print(a)
a.append([66, 77])
a.extend([88, 99])
print(a)
# search
print(a.index(55)) # 4
#print(a.index(100))  # exception
# remove
#	based on pos
a = [11, 22, 33, 44, 55]
print(a.pop())
print(a)
print(a.pop(2))
print(a)
#	based on val
a = [11, 22, 33, 44, 55]
print(a.remove(33)) # None
#print(a.remove(66)) # error

# create a list of n empty lists
n = 5
a = []
i = 0
while i < n :
	a.append([])
	i += 1
print(a)























