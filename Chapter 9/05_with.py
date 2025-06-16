# f = open("hello.txt")
# print(f.read())
# f.close()

# The samme can be written using with statement like this:
with open("hello.txt") as f:
    print(f.read())

# You dont have to explicitly close the file using with statement.