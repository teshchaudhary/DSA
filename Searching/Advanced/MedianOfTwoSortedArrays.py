def getmid(a1, a2):

    l1, l2 = len(a1), len(a2)
    si, ei = 0, l1

    while (si <= ei):
        # Mid element of the smaller array
        i1 = (si + ei) // 2

        # Corresponding element in the larger array
        i2 = ((l1 + l2 + 1)//2 - i1)

        # Maximum of left half in 1st array
        mxl1 = float('-inf') if i1 == 0 else a1[i1-1]
        
        # Minimum of right half in 1st array
        mnr1 = float('inf') if i1 == l1 else a1[i1]

        # Maximum of left half in 2nd array
        mxl2 = a2[i2 - 1]

        # Minimum of right half in 2nd array
        mnr2 = a2[i2]

        if mxl1 <= mnr2 and mxl2 <= mnr1:
            # A check for the lengths to calculate the median

            if (l1+l2) % 2 == 0:
                return (max(mxl1, mxl2) + min(mnr1, mnr2))/2

            else:
                return max(mxl1, mxl2)

        # Which halves to move to
        elif mxl1 > mnr2:
            ei = i1 - 1

        else:
            si = i1 + 1