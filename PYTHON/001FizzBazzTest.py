for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("%d is FizzBazz" % x)
    if x % 3 == 0:
        print("%d is Fiz" % x)
    elif x % 5 == 0:
        print("%d is Bazz" % x)


