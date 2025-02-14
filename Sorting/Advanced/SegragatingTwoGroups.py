# In this type of problem we can segragate different groups in an array like
# Positive and Negative
# Even and Odd
# Ones and Zeros

# Naive Approach
# O(n) Time and Space Complexity
def sort_(arr) :
    n = len(arr)
    temp = [0] * n 
    i = 0 
    for j in range(0,n) :
        if arr[j] < 0 :
            temp[i] = arr[j]
            i += 1 
            
    for j in range(0,n) :
        if arr[j] >= 0 :
            temp[i] = arr[j]
            i += 1 
    arr[:] = temp
    
    print(arr)

# Efficient Solution
# O(1) Space Complexity
# O(n) Time Complexity
# Hoarse Partition

def sort(arr) :
    i,j = -1,len(arr) 
    while True :

        i += 1 
        while arr[i] < 0 :
            i += 1

        j -= 1 
        while arr[j] >= 0 :
            j -= 1 
            
        if i >= j :
            return
        arr[i],arr[j] = arr[j],arr[i]
        
    return arr