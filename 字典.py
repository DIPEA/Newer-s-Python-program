dictionary = {}
count = 1
while count < 4:
    i = input("Add or look up a word(a/1)?")
    if i == 'a':
        x = input("Type the word:")
        y = input("Type the definition:")
        dictionary["x"] = y
        print("Word added!")
    elif i == '1':
        z = input("Type the word:")
        if z == x:
            print(dictionary["x"])
        else:
            print("That word isn't in the dictionary yet.")
    count += 1
