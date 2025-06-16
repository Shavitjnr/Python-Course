with open("log.txt")as f:
    content = f.read()
    print(content)
if("Python" in content):
    print("Yes, Python is present in the file")
else:
    print("No, Python is not present in the file")