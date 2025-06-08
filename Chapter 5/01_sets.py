d = {}
print(type(d))  # This will print the type of the variable 'd', which is a dictionary
print(d)  # This will print the empty dictionary
marks = {
    "Harry": 98,
    "Rohan": 95,
    "Hammad": 93,
    0:"Shavit"   
}
print(marks["Harry"])  # This will print the value associated with the key "Harry"
print(marks["Rohan"])  # This will print the value associated with the key "Rohan"  
print(marks["Hammad"])  # This will print the value associated with the key "Hammad"
print(marks[0])  # This will print the value associated with the key 0, which is "Shavit"
print(marks)  # This will print the entire dictionary
print(type(marks))  # This will print the type of the variable 'marks', which is a dictionary
print(marks.items())
print(marks.keys())  # This will print the keys of the dictionary
print(marks.values())  # This will print the values of the dictionary
print(marks.update({"Shavit": 100}))  # This will update the dictionary by adding a new key-value pair "Shavit": 100
print(marks)  # This will print the updated dictionary after adding the new key-value pair
print(marks.get("Shavit"))  # This will print the value associated with the key "Shavit", which is 100
print(marks)