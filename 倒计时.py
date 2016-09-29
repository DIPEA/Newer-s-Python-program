import time
timer = int(input("Counterdown timer: How many seconds?"))
for i in range(timer, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!")
