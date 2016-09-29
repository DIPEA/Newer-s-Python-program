numBlocks = int(input("How many blocks of stars do you want?"))
numLines = int(input("How many lines in each block?"))
numStars = int(input("How many stars per line?"))
for block in range(1, numBlocks + 1):
    for line in range(1, numLines + 1):
        for star in range(1, numStars + 1):
            print("*")
        print
print
