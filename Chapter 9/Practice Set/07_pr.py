
with open("log.txt")as f:
    lines = f.readlines()
line = 1
for line in lines:
    if("Python" in line):
        print(f"Yes, Python is present in Line no: {line} ")
    else:
        print(f"No, Python is not present in Line no: {line}")