print("Enter 5 names:")
names = []
for name in range(0, 5):
    names.append(input())
print("The names are",names[0],names[1],names[2],names[3],names[4])
a = int(input("Replace one name. Which one?(1-5):"))
names[a-1] = 'Peter'
print("New name:",names[a-1])
print("The names are",names[0],names[1],names[2],names[3],names[4])
