''' write a function that generates a string that is 27 characters long by
choosing random letters from the 26 letters in the alphabet plus the spaceW.
e’ll write another function that will score each generated string by comparing the randomly generated string to the
goal.
A third function will repeatedly call generate and score, then if 100% of the letters are correct we
are done. If the letters are not correct then we will generate a whole new string.To make it easier to
follow your program’s progress this third function should print out the best string generated so far
and its score every 1000 tries.'''

import random



ab = list("abcdefghijklmnopqrstuvwxyz")


def generate(x):
    y = random.sample(x, len(x))
    return x, y

def score (x,y):
    sco = 0
    for i in range (len(x)):
        if x[i] == y[i]:
            sco+=1
    return sco*100/27

def test():
    rt1, rt2 = generate(ab)
    s = score(rt1, rt2)
    if s == 100:
        return f"matched - {s}"
    else:
        return s


print(test())

x, y = generate(ab)
print(cmp(tuple(x),tuple(y)))



