# Recursive Solution
def minPages(arr,n,k):
    
    # Sum up till the first partition
    if k == 1:
        return sum(arr[0:n])
    
    # Extra case
    if n == 1:
        return arr[0]
    
    res = float('inf')
    
    # Check for each partitions possible
    for i in range(1, n):
        res = min(res,max(minPages(arr,i,k-1),sum(arr[i:n])))
        
    return res

# Efficient Solution
# Binary Search

# Allocate Minimum pages (Binary Search)

# By feasibility it means that if we require more students than given or are the given students enough
# req variable is taking care of this
# s is th current sum of elements
def isfeasible(arr,k,ans) :
    req, s = 1, 0
    for i in range(len(arr)) :
        # Keep checking if the increasing sum is still lower than the mid point (ans)
        if (s + arr[i]) > ans :
            # If it increases then we need one more student
            req += 1 
            s = arr[i]
        else :
            # Keep increasing
            s += arr[i]
    
    # If the required students are less than or equal to given students then it is feasible otherwise not
    return (req <= k)
    
def minpages(arr,k) :
    n = len(arr)
    # Upper bound as we assign all the books to a single student
    s = sum(arr)

    # Minimum bound that we give the book with maximum pages to a student.
    mx = max(arr)

    low,high = mx,s
    res = 0 
    while low <= high :
        mid = (low + high) // 2
        # If it is fesible we keep looking for lower values by moving to the left side
        if (isfeasible(arr,k,mid)) :
            res = mid
            high = mid - 1 
        
        # If the required students are more it means we need to move to the right side
        else :
            low = mid + 1 
    return res
