s = {1, 2, 3, 4, 5,'Shavit'}
print(s, type(s))  # This will print the original set
s.add(6)  # Adding an element to the set
print(s)  # This will print the updated set
print(len(s))  # This will print the number of elements in the set
print(s)
s.remove(4)  # This will remove the element 4 from the set
print(s)  # This will print the set after removing the element
s.pop()  # This will remove and return an arbitrary element from the set
print(s)  # This will print the set after popping an element