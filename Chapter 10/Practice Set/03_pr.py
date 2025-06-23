class Demo:
    a = 4

o = Demo()
o.a = 0
print(o.a)  # print the class attribut bcause instance attribute is not present 

o.a = 0     # modifying the instance attribute
print(o.a)  # print the instance attribute
print(Demo.a)  # print the class attribute