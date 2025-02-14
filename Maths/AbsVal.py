def absolute(I):
    if I < 0:
        I *= -1
        return I
    else:
        return I

print(absolute(-5))