# Count how many bits should be flipped in order to make two numbers same

def countBitsFlip(a, b):
    count = 0
    while a or b:
        if (a & 1) != (b & 1):
            count += 1

        a >>= 1
        b >>= 1
    return count

print(countBitsFlip(5,10))