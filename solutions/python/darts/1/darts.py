import math

def score(x, y):
    d = math.sqrt(x*x + y*y)
    if d > 10:
        return 0
    elif d > 5:
        return 1
    elif d > 1:
        return 5
    else:
        return 10