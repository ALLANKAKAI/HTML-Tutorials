def odd(x):  # x.sort(key=lambda x: x % 2 == 0, reverse=True)
    return x % 2 == 0


def oddlist(b):
    k = sorted(b)    # sorting the list first to get small to big
    k.sort(key=odd, reverse=True)  # sorting to get odd and even
    return k


x = [1, 3, 4, 5, 6, 6, 6, 7, 5, 8, 9, 9]
print("sorted:", oddlist(x))
