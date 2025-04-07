def minimumJumps(arr, n):
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    jumps = 0
    l = 0
    r = 0

    while r < n - 1:
        jumps += 1
        farthest = 0

        for i in range(l, r + 1):
            farthest = max(farthest, i + arr[i])
        
        if farthest == r:
            return -1

        l = r + 1
        r = farthest
       
    return jumps