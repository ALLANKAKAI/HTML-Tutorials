def new_price(old_price, discount):
    x = (1-discount)*old_price
    s = format(x, ".2f")
    return s


car = new_price(2.89, 0.2)
print(car)
