import time
timer = int(input("Counterdown timer: How many seconds?"))
for i in range(timer, 0, -1):
    print(i)
    for star in range(0, i):
        print("*")
    time.sleep(1)
print
print("BLAST OFF!")        
