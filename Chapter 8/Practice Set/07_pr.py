def rem(l, word):
    n = []
    for item in l:
        if item == word:
            if not(item.strip(word)):
                return n
l = ["Shavit","Rohan","Shubham", "an"]
print(rem(l,"an"))