money = ['quarters','dimes','nickels','pennies']
def caculate(money):
    total = (money[0] * 25 +money[1] * 10 + money[2] * 5 + money[3]) / 100
    return total
money[0] = int(input("quarters:"))
money[1] = int(input("dimes:"))
money[2] = int(input("nickels:"))
money[3] = int(input("pennies:"))
my_total = caculate(money)
print("total is $",my_total)
