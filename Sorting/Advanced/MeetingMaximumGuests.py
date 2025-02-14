def maxguests(arrivals,departures):
    arrivals.sort()
    departures.sort()

    curr = res = 1
    i, j = 1, 0
    while (i < len(arrivals) and j < len(departures)):
        if arrivals[i] <= departures[j]:
            curr += 1
            i += 1
        
        else:
            curr -= 1
            j += 1

        res = max(res, curr)
    
    return res