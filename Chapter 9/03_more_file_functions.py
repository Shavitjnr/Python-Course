f = open("hello.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))
# line4 = f.readline()
# print(line4, type(line4))
# line5 = f.readline()
# print(line5 =="")

lines = f.readlines()
while(lines != ""):
    print(lines)
    lines = f.readline()
f.close()