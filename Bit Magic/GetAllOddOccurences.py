def count(arr):
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1

        if count % 2 != 0:
            print(i, end=" ")


count([1, 1, 2, 2, 3, 3, 4])
