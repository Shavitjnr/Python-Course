friends = ["Harry", "Ron", "Hermione", 5, 345, False, "Banana", "Orange"]
print(friends)  # This will print the original list
friends[6] = "Mango"  # Replace "Banana" with "Mango"
print(friends)  # This will print the modified list
friends[0] = "Shavit"  # Change the first element to "Shavit"
print(friends)  # This will print the modified list with "Shavit" as the first element
print(friends[0:4])  # Print the first four elements of the list
print(friends[0:4:2])  # Print the first four elements of the list with a step of 2
friends.append("Pineapple")  # Append "Pineapple" to the end of the list
print(friends)  # This will print the list after appending "Pineapple"
l1 = [1,2,3,4,5,6,7,8,9,10]
l1.sort()  # Sort the list in ascending order
print(l1)  # This will print the sorted list
l1.reverse()  # Reverse the list in place
print(l1)  # This will print the reversed list
l1.insert(-1, 0)  # Insert 0 at the beginning of the list
print(l1)  # This will print the list after inserting 0 at the beginning
l1.remove(0)  # Remove the first occurrence of 0 from the list
print(l1)  # This will print the list after removing 0
l1.pop(3)  # Remove the last element from the list
print(l1)  # This will print the list after removing the last element
l1.reverse()  # Reverse the list in place
print(l1)  # This will print the reversed list
l1.clear()  # Clear the list, removing all elements
print(l1)  # This will print an empty list