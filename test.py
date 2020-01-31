def max(x,y,z):
    if x > y:
        y = x
        if x > z:
            return x
    elif y > x:
        if y > z:
            return y
        elif z > y:
            return z
print(max(4,6,3))