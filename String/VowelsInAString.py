def func(s):
    check = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s:
        if i in check:
            count += 1

    return count

print(func("Tortoise"))