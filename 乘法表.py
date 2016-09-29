i=int(input("Which multiplication table would you like?"))
j=int('1')
k=int(input("How high do you want to go?"))
print("Here's your table:")
while j <= k:
    print(i,"x",j,"=",i*j)
    j += 1
