def mylist(x):
    evenlist = []
    for item in x:
        if item % 2 == 0:
            evenlist.append(item)
    return evenlist


x = [1, 3, 4, 5, 6, 6, 6, 7, 5, 8, 9, 9]
print(x)
print("evenlist:", mylist(x))

def kk(x):
    return list(filter(lambda p:p%2==0,x))


print(kk(x))
