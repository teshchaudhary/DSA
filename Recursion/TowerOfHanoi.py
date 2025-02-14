def toh(n, a, b, c):

    if n == 1:
        print(f"move disk {n} from rod {a} to rod {c}")
        return 1

    count = toh(n-1, a, c, b)
    print(f"move disk {n} from rod {a} to rod {c}")
    count += toh(n-1, b, a, c)
    return count + 1


print(toh(3, 1, 2, 3))

