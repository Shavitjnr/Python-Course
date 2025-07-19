# myList = [1, 2, 3, 4, 5]
# myList = [x * x for x in myList]
# print(myList)

myList = [1, 2, 3, 4, 5]

squaredList = []
for item in myList:
    squaredList.append(item * item)
print(squaredList)