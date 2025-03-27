def minimumPlatform(arr, dep):
    n = len(arr)
    events = []
    
    for i in range(n):
        events.append((arr[i], 1))
        events.append((dep[i], -1))
    
    # if the departure and arrival are same we will need one more platform
    # ex: arr = [90, 100] and dep[100, 120]
    # so we will need two platforms
    events.sort(key = lambda x: (x[0], -x[1]))
    
    res = 0
    curr = 0
    for i in range(2*n):
        curr += events[i][1]
        res = max(curr, res)
    
    return res