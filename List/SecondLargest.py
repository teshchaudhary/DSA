def secondLargest(l):
    if len(l) <= 1:
        return None

    largest = l[0]
    sLargest = None

    for i in l[1:]:
        if i > largest:
            sLargest = largest
            largest = i

        elif i != largest:  # handles the duplicate values
            # case for none can be [2,2,1]
            # As Second largest was not set until index 1
            if sLargest == None or sLargest < i:
                sLargest = i

    return (sLargest, largest)


print(secondLargest([5, 12, 15, 20, 20]))
