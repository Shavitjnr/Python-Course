# Write a program to read the text from a given file poems.txt and find out whether it contains the work twinkle.
# with open("poems.txt", "w") as f:
#     f.write("Twinkle Twinkle!! \n")
#     f.write("How are you? \n")

f = open("poems.txt", "r")
if "Twinkle" in f.read():
    print("The word Twinkle is present in the file")
else:
    print("The word Twinkle is not present in the file")
f.close()

