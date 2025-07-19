# Mearching of dict 
# dic1 = {'a': 1, 'b': 2 }
# dic2 = {'b': 3, 'c': 4 }
# merged_dict = {**dic1, **dic2}
# merged_dict = dic1 | dic2

# print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using two with ( using with and open multiple files )

with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    content1 = f1.read()
    content2 = f2.read()
    print(content1)
    print(content2)
    