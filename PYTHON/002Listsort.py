def evenlist(mylist):
    srt = sorted(mylist)
    return sorted(srt, key=lambda x:x%2==0, reverse=True)


x = [1, 34, 90, 79, 2, 3, 1, 4, 5, 8, 2, 77, 108, 99, 7]
print("evenlist2:", evenlist(x))






