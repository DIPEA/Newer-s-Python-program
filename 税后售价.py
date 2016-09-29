def caculateTax(price, Tax_rate):
    total = price + (price * Tax_rate)
    return total

my_price = float(input("Enter a price:"))

totalPrice = caculateTax(my_price, 0.06)
print("price =",my_price,"total price =",totalPrice)
