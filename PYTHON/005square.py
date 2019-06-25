def sqlist(x):
    newlist = []
    for item in x:
        y = item * item
        newlist.append(y)
    return newlist


kk = [1, 3, 5, 2, 8]
print(sqlist(kk))

m = list(map(lambda x: x ** 3, kk))


def dd(kk):
    return [x ** 2 for x in kk]




print("Triple:", m)

kk2 = [9, 89, 78, 6, 7]
p = list(map(lambda x, y: x + y, kk, kk2))
print("p:", p)


def add(lst1, lst2):
    return list(map(lambda x, y: x + y, lst1, lst2))


kk = [1, 3, 5, 2, 8]
kk2 = [9, 89, 78, 6, 7]
x = add(kk, kk2)
print(x)
