# An element is considered a majority element if the element comes more than the half of the length of the array (freq(n) > length(arr)/2)
# Return the index of such element

# Naive Solution
# O(n^2)

def func1(arr):
    l = len(arr)
    threshold = l//2

    for i in range(len(arr)):
        count = 1

        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > threshold:
            return i

    return -1

# Efficient Solution
# Boyer-Moore Majority Voting Algorithm
# We increase the count if the canditate element is equal to current element
# Otherwise decrease the count
# This works as if we the count decreases it means there are votes for other as well that reduces the chances to win

# We can also infer that if we divide the array into two
# One containing all the elements that cancels the votes
# Other containing that didn't cancel the votes
# We can see that in the first array will have pairs which can cancel each other if the pair is same as well even then it can come for maximum (n/2) times not more than that

# O(n)


def func2(arr, n):
    candidate_index = 0
    votes = 1

    # Finding a candidate
    for i in range(n):
        if arr[candidate_index] == arr[i]:
            votes += 1
        else:
            votes -= 1
        
        if votes == 0:
            candidate_index = i
            votes = 1

    # Checking if majority candidate occurs more than n/2 times
    votes = 0

    for i in range(n):
        if (arr[candidate_index] == arr[i]):
            votes += 1

    if (votes < n // 2):
        candidate_index = -1
        
    return candidate_index


# Imagine a condition when our majority elements can be if those elements have apperared more than (l/3) times

# We can use Boyes Moore's Voting Algorithm again but with a little alteration
# If the majority criteria becomes l/3 then, only two majority elments can be there

def majorityElementII(arr):
    res = []
    l = len(arr)
    c1 = c2 = 0
    cand_1 = cand_2 = float('-inf')

    for num in arr:
        if num == cand_1:
            c1 += 1
        
        elif num == cand_2:
            c2 += 1
        
        elif c1 == 0 and cand_2 != num:
            c1 = 1
            cand_1 = num
        
        elif c2 == 0 and cand_1 != num:
            c2 = 1
            cand_2 = num
        
        else:
            c1 -= 1
            c2 -= 1
    
    count_1 = count_2 = 0
    for num in arr:
        if num == cand_1:
            count_1 += 1
        
        if num == cand_2:
            count_2 += 1
    
    if count_1 > l // 3:
        res.append(cand_1)

    if count_2 > l // 3:
        res.append(cand_2)
    
    return res