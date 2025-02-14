# def OddOccurence(arr):
#     for i in arr:
#         c = arr.count(i)

#         if c%2 != 0:
#             return i

# def OddOccurence(arr):
#     for i in arr:
#         count = 0

#         for j in arr:
#             if i == j:
#                 count += 1

#         if count % 2 != 0:
#             return i


# -------- Efficient Solution --------
def OddOccurences(arr):
    g1 = 0
    g2 = 0

    xors = 0
    for i in arr:  # Getting XOR of all elements in array
        # This will contain the XOR of two odd occuuring elements
        xors = xors ^ i

    sb = (xors) & ~(xors-1)  # To find rightmost set bit

    # The idea to find the rightmost set bit is to divide the numbers into two groups
    # E.g. The odd occuring elements are 5 and 6, XOR of 5 and 6 is 3
    # Now Xor of 3 with ~(3-1) gives the rightmost set bit

    # Now this means at this place the bit is different thats why the negation made the bits same and hence AND as 1 and thats how it makes two groups

    # g1 = [3,3,5,7,7] # XOR of all the elements here will give 5 as for all these elements the right most set bit is 1

    # g2 = [4,4,4,4,6] # XOR of all the elements here will give 6 as for all these elements where the righmost set bit of above elements is 1, here the bit is not set

    for i in arr:

        if i & sb != 0:
            g1 ^= i

        else:
            g2 ^= i

    return (g1, g2)


arr = [1, 2, 3, 2, 1, 4]
print(OddOccurences(arr))
