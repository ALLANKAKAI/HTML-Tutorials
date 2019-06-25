def addMarks(x):
    for key in x.keys():
        if x[key] <= 40:
            x[key] += 20
    return x


stream5 = {"A": 25, "B": 90, "C": 66, "D": 20}
print(stream5.values())
print(addMarks(stream5))
print(stream5['A'])

def addMarks(x):
    if x<= 40:
        x+= 20
    return x


